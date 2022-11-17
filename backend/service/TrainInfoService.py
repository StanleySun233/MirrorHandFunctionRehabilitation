import tool


class TrainInfoService(tool.Service.Service):
    def __init__(self, model: tool.Model):
        super().__init__(model)

        self.msg['0'] = '查询成功'

    def listByDate(self, attrs):
        sheet = self.list(dump=True, isLike=True)
        return sheet
