a = input()
a = a.replace(' ','').replace('\n','')
a = a.split(';')
res = []
for i in range(0, len(a)):
    if '事件类型' in a[i]:
        res.append(a[i:i+2])

d = {}
for i in range(len(res)):
    d[res[i][0]] = res[i][-1]

res = ['{}: {}'.format(i, d[i]) for i in d.keys()]
for i in res:
    print(i)