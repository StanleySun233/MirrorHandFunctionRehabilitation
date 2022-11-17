import tool


class VASService(tool.Service.Service):
    def __init__(self, model: tool.Model):
        super().__init__(model)

        self.msg['0'] = '查询成功'
