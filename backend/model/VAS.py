import tool


class VAS(tool.Model.Model):
    def __init__(self, table, sqlClient: tool.SqliteHelper):
        super().__init__(table, sqlClient)
