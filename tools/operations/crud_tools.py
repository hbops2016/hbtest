from db.crud_base import CRUDBase
from tools.models import operation_signal_record


class CRUDSignalrecord(CRUDBase):
    pass


Signal = CRUDSignalrecord(operation_signal_record)