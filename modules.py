###########################datetime###############################
from datetime import datetime

now = datetime.now()

print(now)

#datetime转换为timestamp
dt = datetime(2015, 4, 19, 12, 20)
print(dt.timestamp())

#timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

#timestamp也可以直接被转换到UTC标准时区的时间：与北京时间差8小时
print(datetime.utcfromtimestamp(t))

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换为str
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%A, %B %d %H:%M'))

#关于时间格式的转化 https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

###########################collections###############################
teststr = "dsklsdjflks aspdfjpqwef jhywednbskdl;e frnoodf kdkja lkjfgg;rkfg jkqrlk"

result = {}
for ch in teststr:
        if ch == ' ':
            continue
        result[ch] = result.get(ch, 0) + 1;

print(result)
print(result.items())
print(sorted(result.items()))
print(sorted(result.items(),key=lambda x:x[1]))
print(sorted(result.items(),key=lambda x:x[1],reverse=True))
print(sorted(result.items(),key=lambda x:x[1],reverse=True)[:3])

from collections import Counter
res = Counter()
for ch in teststr:
    if ch == ' ':
        continue
    res[ch] = res[ch] + 1

print(res)
print(sorted(res.items(),key=lambda x:x[1],reverse=True)[:3])

###########################hashlib###############################
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hasnlib'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in python hasnlib?'.encode('utf-8'))
print(md5.hexdigest())

#对md5加盐，增加破解难度md5(message + salt)
slat = 'md5salt'
str= 'how to use md5 in python hasnlib?'

md5 = hashlib.md5()
md5.update(str.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update(str.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in python hasnlib?md5salt'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update((str+slat).encode('utf-8'))
print(md5.hexdigest())

#使用随机验证码，(随机盐)
import hmac
message = b'how to use md5 in python hasnlib?'
key = b'md5salt'
h = hmac.new(message, key, digestmod = 'MD5')
print(h.hexdigest())

h = hmac.new(str.encode('utf-8'), slat.encode('utf-8'), digestmod = 'MD5')

print(h.hexdigest())


###########################urllib###############################
from urllib import request

with request.urlopen("http://apilocate.amap.com/position?accesstype=0&cdma=0&key=8eca96227a6489db9af57d01edfe27cc&bts=460,04,6257,27781411,-95") as f:
    data = f.read()
    print("Status",f.status, f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print('Data:',data.decode('utf-8'))

from urllib import request,parse

print("Login to weibo.cn")
# email = input('Email:')
# passwd = input('Password:')
email = 'test'
passwd = 'test'
login_data = parse.urlencode(
    [
        ('username',email),
        ('password',passwd),
        ('entry','mweibo'),
        ('client_id',''),
        ('savestate','1'),
        ('ec',''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ]
)

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:',f.status, f.reason)
    for k,v in f.getheaders():
        print('%s,%s' % (k,v))
    print('Data:',f.read().decode('utf-8'))

###########################requests###############################
import requests

r = requests.get('https://www.douban.com/')
print('Status:',r.status_code, r.reason)
# print(r.text)
print(r.url)
print(r.encoding)

r = requests.get('https://www.douban.com/serrch', params={'q':'python'})
print(r.url)
print(r.content)

#requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
r = requests.get("http://apilocate.amap.com/position?accesstype=0&cdma=0&key=8eca96227a6489db9af57d01edfe27cc&bts=460,04,6257,27781411,-95")
print('text:',r.text)
print('json:',r.json())

h = r.headers
print(h)
for k, v in h.items():
    print(k,': ', v)