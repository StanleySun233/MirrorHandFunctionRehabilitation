with open('trans.txt', 'r', encoding='utf-8') as f:
    sheet = [i.replace("\n", "").split(".")[1] for i in f.readlines()]

d = {}

for i in sheet:
    name_cn, name_en = i.split(":")
    d[name_en] = name_cn
    d[name_cn] = name_en

d = str(d)
print(d.encode("utf-8").decode('utf-8'))