import tool


class PatientInfoService(tool.Service.Service):
    def __init__(self, model: tool.Model):
        super().__init__(model)

        self.msg['0'] = '查询成功'

    def listByName(self, data: dict = None):
        if data is None:
            name = ''
        else:
            name = data['name']
        col = ['id', 'name', 'sex', 'age', 'illness']
        sheet = self.list(attrs={'name': name}, val=col, dump=True, isLike=True)
        return sheet
