with open('trans.txt', 'r', encoding='utf-8') as f:
    sheet = [i.replace("\n", "").split(".")[1] for i in f.readlines()]

d = {}

for i in sheet:
    print(i)
    name_cn, name_en = i[0], i[1]
    d[name_en] = name_cn
    d[name_cn] = name_en

d = str(d)
print(d.encode("utf-8").decode('utf-8'))
