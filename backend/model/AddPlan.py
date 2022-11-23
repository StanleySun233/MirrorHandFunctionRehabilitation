import tool


class AddPlan(tool.Model.Model):
    def __init__(self, table, sqlClient: tool.SqliteHelper):
        super().__init__(table, sqlClient)
