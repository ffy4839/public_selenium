# a = input()
# a = a.replace(' ','').replace('\n','')
# a = a.split(';')
# res = []
# for i in range(0, len(a)):
#     if '事件类型' in a[i]:
#         res.append(a[i:i+2])
#
# d = {}
# for i in range(len(res)):
#     d[res[i][0]] = res[i][-1]
#
# res = ['{}: {}'.format(i, d[i]) for i in d.keys()]
# for i in res:
#     print(i)
import json
import time

data = [{'domain': '192.168.18.27', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/sgp/', 'secure': False, 'value': '5C7F115992CBDC0FD44B9C62F25ED907'}, {'domain': '192.168.18.27', 'expiry': 1571473656, 'httpOnly': False, 'name': 'userName', 'path': '/sgp/login', 'secure': False, 'value': '999'}, {'domain': '192.168.18.27', 'expiry': 1571473656, 'httpOnly': False, 'name': 'rmbUser', 'path': '/sgp/login', 'secure': False, 'value': 'true'}]


def write(data):
    with open('cookies.json','w') as f:
        json.dump(data,f)


def read():
    with open('cookies.json','r') as f:
        r = f.read()
        return json.loads(r)

if __name__ == '__main__':
    a = write(data)
    time.sleep(1)
    print(read())