import json
import random

import tool


class SpaceImageConfigService(tool.Service.Service):
    def __init__(self, model: tool.Model):
        super().__init__(model)

        self.msg['0'] = '查询成功'

    def getPic(self, data):
        sheet = self.list(attrs={'difficult': data['difficult']}, dump=False)

        sheet = random.sample(sheet, min(len(sheet), int(data['pic_number'])))
        return json.dumps({"data": sheet, "code": 1}, ensure_ascii=False)

