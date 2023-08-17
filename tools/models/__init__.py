from typing import Text

from db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, text, Boolean, JSON, ForeignKey


class operation_signal_record(Base):
    __tablename__ = "operation_signal_record"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    operation_name = Column(String, nullable=False, index=True)
    operation_data = Column(JSON, nullable=False)
    operation_environment = Column(String, nullable=False, index=True)
    operation_api_res = Column(String, nullable=False, index=True)
    operation_time = Column(DateTime, nullable=True, server_default=text('current_timestamp'))




