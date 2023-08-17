from fastapi.encoders import jsonable_encoder
from sqlalchemy import text, or_, and_
from sqlalchemy.orm import Session

from db import SessionLocal
from typing import List


class CRUDBase:

    def __init__(self, model):
        self.model = model

    def getByID(self, id):
        with SessionLocal() as session:
            return session.query(self.model).filter(self.model.id == id).first()

    def getBytype(self, function_type):
        with SessionLocal() as session:
            return session.query(self.model).filter(self.model.function_type == function_type).all()

    def page(self, page: int = 1, limit: int = 10, **kwargs):
        """
        可选条件的分页查询
        :param page: 起始页
        :param limit: 数据条数
        :param kwargs: 查询条件
        :return: 数据 及 数据总数
        """
        listCondition = [f"self.model.{k}.like('%{v}%')" for k, v in kwargs.items() if v is not None]
        condition = []
        for item in listCondition:
            condition.append(eval(item))
        with SessionLocal() as session:
            query = session.query(self.model).filter(or_(*condition))
            total = query.count()
            items = query.limit(limit).offset((page - 1) * limit).all()
            return items, total

    def save(self, schema_in):
        # 做兼容的类型转换
        schema_in_data = jsonable_encoder(schema_in)
        # 将schema_in_data转换成数据库对象
        db_obj = self.model(**schema_in_data)
        with SessionLocal() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def updateByID(self, id, schema_in):
        db_obj = self.getByID(id=id)
        obj_data = jsonable_encoder(db_obj)
        if isinstance(schema_in, dict):
            update_data = schema_in
        else:
            # exclude_unset=True  过滤不需要更新的数据
            update_data = schema_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        with SessionLocal() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
            return db_obj

    def removeByID(self, id):
        """
        根据id删除数据
        :param id: id号
        :return:
        """
        with SessionLocal() as session:
            db_obj = session.query(self.model).get(id)
            if db_obj is None:
                return db_obj
            session.delete(db_obj)
            session.commit()
            return db_obj

    # 批量删除
    def removeByIDs(self, ids: List[int]):
        """
        根据id删除多条数据
        :param ids: ids号
        :return:
        """
        with SessionLocal() as session:
            session.query(self.model).filter(self.model.id.in_(ids)).delete(synchronize_session=False)
            session.commit()

    def ListBySqlCondition(self, condition: str):
        '''
        根据查询条件返回制定的数据
        '''
        with SessionLocal() as session:
            return session.query(self.model).filter(text(condition)).all()

    def ListByDictCondition_Or(self, exactMath=False, **kwargs):
        if exactMath:
            condition = {k: v for k, v in kwargs.items() if v is None}
            with SessionLocal() as session:
                return session.query(self.model).filter_by(**condition).all()
        else:
            listCondition = [f"self.model.{k}.like('%{v}%')" for k, v in kwargs.items() if v is not None]
            condition = []
            for item in listCondition:
                condition.append(eval(item))
            with SessionLocal() as session:
                return session.query(self.model).filter(or_(*condition)).all()
