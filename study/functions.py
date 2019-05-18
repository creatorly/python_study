from datetime import datetime

def fun():
    print("done")

print("begin time:",datetime.now())
fun()
print("end time:",datetime.now())


def callfun(func):
    print("begin time:", datetime.now())
    func
    print("end time:", datetime.now())


def test():
    print("test")

callfun(test)

########################排序函数sorted############################
#Python内置的sorted()函数就可以对list进行排序：
age = [1, 3, 5, 6, 7, 2, 0, -2, 4]
print(sorted(age))

print(sorted(age, key = abs))     # 求绝对值后再排序

def below(n):
    return n * n

print(sorted(age, key = below))   # 求平方后再排序
print(sorted(age, key = lambda n:n * n ))

age = {'0': 1, '1': 3, '2': 5, '3': 6, '4': 7, '5': 2, '6': 0, '7': -2, '8': 4}
print(age)
print(age.items())
print(sorted(age.items()))
print(sorted(age.items(), reverse = True))
print(sorted(age.items(), key = lambda x:x[1]))

#######################匿名函数lambda############################
#通俗的讲就是没有名字的函数，有个好处，因为函数没有名字，不必担心函数名冲突

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda n:n % 2 == 1, range(1, 20)))
print(L)

#######################修饰器Decorator###########################
#无参数函数装饰器
import functools

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

print(now())
print(now.__name__)

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

print(now())
print(now.__name__)

#有参数函数装饰器
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('start')
def now():
    print('2015-3-25')

print(now())
print(now.__name__)

import time, functools

def metric(func):
    if callable(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start = time.time()
            print("%s start" %  (func.__name__))
            rts = func(*args, **kw)
            print("%s end" % (func.__name__))
            end = time.time()
            print('%s executed in %.4f ms' % (func.__name__, end - start))
            return rts
        return wrapper
    else:
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                start = time.time()
                print("%s start" % (fn.__name__))
                rts = fn(*args, **kw)
                print("%s end" % (fn.__name__))
                end = time.time()
                print('%s %s executed in %.4f ms' % (func, fn.__name__, end - start))
                return rts
            return wrapper
        return decorator

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

@metric('start')
def test(x, y, z):
    time.sleep(0.3456)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
t = test(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
elif t != 7986:
    print('测试失败!')


#######################练习###########################
#一个字符串中字母出现的次数，出现前三的字幕
str = "dsffsd lksjdflkjsdalje[p weolds sdjfsdkljfj[peow-0w0w9eurerhfgkmn;xalsd;aoierp9483-730lkdsla"

L = {}

for char in str:
    if char == ' ':
        continue
    L[char] = L.get(char,0) + 1

print(L)
print(sorted(L.items(), key=lambda x:x[1], reverse=True)[:3])
