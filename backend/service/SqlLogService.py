import tool


# 二次开发再添加使用

class SqlLogService(tool.Service.Service):
    def __init__(self, model: tool.Model):
        super().__init__(model)

        self.msg['0'] = '查询成功'
