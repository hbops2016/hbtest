from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse


class R:
    @staticmethod
    def ok(code=0, message="success", data=None):
        data = jsonable_encoder(data)
        return JSONResponse(status_code=200,
                            content={
                                "code": code,
                                "message": message,
                                "data": data
                            })

    @staticmethod
    def error_404(message="数据不存在"):
        return JSONResponse(status_code=404,
                            content={
                                "code": 404,
                                "message": message,
                            })

    @staticmethod
    def error_422(message="操作失败"):
        return JSONResponse(status_code=422,
                            content={
                                "code": 422,
                                "message": message,
                            })

    @staticmethod
    def error_403(message="参数错误或参数不存在"):
        return JSONResponse(status_code=403,
                            content={
                                "code": 403,
                                "message": message,
                            })


    @staticmethod
    def error_405(message="空数据"):
        return JSONResponse(status_code=405,
                            content={
                                "code": 405,
                                "message": message,
                            })