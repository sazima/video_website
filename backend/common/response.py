from django.http import JsonResponse


class Response(JsonResponse):
    code = 200
    msg = ''

    def __init__(self, data=None, code=None, msg=None, *args, **kwargs):
        return_dict = {
            'code': code or self.code,
            'msg': msg or self.msg,
            'data': data or {}
        }
        super().__init__(return_dict, *args, **kwargs)


class NotFoundResponse(Response):
    code = 404
    msg = '不存在'


class NotLoginResponse(Response):
    code = 403
    msg = '未登录'
