import tool


class PatientInfo(tool.Model.Model):
    def __init__(self, table, sqlClient: tool.SqliteHelper):
        super().__init__(table, sqlClient)

    def select(self, attrs=None, val=None, mult=True, isLike=False):
        res = super(PatientInfo, self).select(attrs, val, mult, isLike)
        if 'illness_site' in val:
            for i in range(len(res)):
                res[i]['illness_site'] = res[i]['illness_site'].split(',')
        return res

    def selectById(self, ids):
        res = super(PatientInfo, self).selectById(ids)
        res['illness_site'] = res['illness_site'].split(',')
        return res
