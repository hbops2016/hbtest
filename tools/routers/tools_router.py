from fastapi import APIRouter, Depends

from extensions import r
from tools.schemas.signal_schema import SignalSchema, SignalCreateSchema
from extensions.r import R
from tools.models import operation_signal_record
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from db import SessionLocal
from tools.schemas import signal_schema
from tools.operations.crud_tools import Signal as crud

from common.signal_resp import request
from config.settings import settings

router = APIRouter()


@router.post('/bot/signal/listener', response_model=SignalSchema)
def create_signal_operation(item: dict):
    if item is None:
        return R.error_405()
    resp = None
    if item['operation_environment'] == 'dev':
        resp = request(settings.SIGNAL_HOST_DEV, settings.SIGNAL_KEY_DEV, settings.SIGNAL_SECRET_DEV, 'POST',
                       '/api/v1/bot/signal/listener', None,item["operation_data"])
    elif item['operation_environment'] == 'uat':
        resp = request(settings.SIGNAL_HOST_UAT, settings.SIGNAL_KEY_UAT, settings.SIGNAL_SECRET_UAT, 'POST',
                       '/api/v1/bot/signal/listener', None,item["operation_data"])

    # item.pop('operation_time')
    item['operation_api_res'] = resp.text
    signal = crud.save(schema_in=item)
    return R.ok(data=signal)


    # 将schema_in_data转换成数据库对象
