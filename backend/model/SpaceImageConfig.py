import tool


class SpaceImageConfig(tool.Model.Model):
    def __init__(self, table, sqlClient: tool.SqliteHelper):
        super().__init__(table, sqlClient)
