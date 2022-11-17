import tool


# 二次开发再添加使用

class UserInfo(tool.Model.Model):
    def __init__(self, table, sqlClient: tool.SqliteHelper):
        super().__init__(table, sqlClient)
