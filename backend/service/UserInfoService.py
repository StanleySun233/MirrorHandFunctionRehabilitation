import json

import tool


class UserInfoService(tool.Service.Service):
    def __init__(self, model: tool.Model):
        super().__init__(model)

        self.msg['0'] = '账号或密码错误'
        self.msg['1'] = '登陆成功'
        self.msg['2'] = '账号不存在'
        self.msg['3'] = '注册成功'
        self.msg['4'] = '账号已经存在'
        self.msg['5'] = '修改成功'
        self.msg['6'] = '成功'

    def login(self, attrs):
        result = self.result.copy()
        account = attrs['account']
        password = attrs['password']
        flag = self.isExist({'account': account})
        if flag:
            acc = self.list(attrs={'account': account}, dump=False)[0]
            if password == acc['password']:
                result['code'] = 1
                result['msg'] = self.msg['1']
                result['data'] = acc['id']
            else:
                result['code'] = 0
                result['msg'] = self.msg['0']
        else:
            result['code'] = 0
            result['msg'] = self.msg['2']

        return json.dumps(result, ensure_ascii=False)

    def register(self, attrs):
        result = self.result.copy()
        account = attrs['account']
        flag = self.isExist({'account': account})
        if flag:
            result['code'] = 0
            result['msg'] = self.msg['4']
        else:
            result['data'] = self.insert(attrs, dump=False)
            result['code'] = 1
            result['msg'] = self.msg['3']

        return json.dumps(result, ensure_ascii=False)

    def forget(self, attrs):
        result = self.result.copy()
        account = attrs['account']
        password = attrs['password']
        flag = self.isExist({'account': account})
        if flag:
            result['data'] = self.updateById(flag, {'password': password}, dump=False)
            result['code'] = 1
            result['msg'] = self.msg['5']
        else:
            result['code'] = 0
            result['msg'] = self.msg['2']

        return json.dumps(result, ensure_ascii=False)

    def getAccountById(self, data):
        result = self.result.copy()
        ids = data['id']
        flag = self.isExist({'id': ids})
        if flag:
            account = self.list(attrs={'id': ids}, dump=False)[0]
            del account['password']
            result['data'] = account
            result['code'] = 1
            result['msg'] = self.msg['6']
        else:
            result['code'] = 0
            result['msg'] = self.msg['2']
        pass
        return json.dumps(result, ensure_ascii=False)