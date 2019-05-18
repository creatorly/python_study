

num = 1
string = '1'
num2 = int(string)
print(num + num2)

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)  # 'bang!'*4
print(total)
total2 = word.replace(word[:4],'**##')
print(total2)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search) + 1 ) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search) + 1 ) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')

#city = input("write down the name of city:")
#url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

#############################条件#############################
age=22
if age <= 18:
    print("your age is",age);
    print("child")
elif age >= 26:
    print("are you afraid")
else:
    print("it's ok")
##############################################################

#############################循环#############################
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in (1,2,3,4,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)


# 原答案没有指出三位数的数量，添加无重复三位数的数量
d=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (a!=c) and (c!=b):
                d.append([a,b,c])   #list
print ("总数量：", len(d))
print (d)
##############################################################

#############################列表#############################
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print("classmates len", len(classmates))
print("classmates[0]", classmates[0])

classmates.append('Adam')     #插入
print(classmates)

classmates.insert(1, 'Jack') #插入指定位置
print(classmates)

classmates.pop(2)             #删除指定位置
print(classmates)
##############################################################

#############################字典#############################
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print (dict['one'])  # 输出键为'one' 的值
print (dict[2])  # 输出键为 2 的值
print (tinydict)  # 输出完整的字典
print (tinydict.keys()) # 输出所有键
print (tinydict.values())  # 输出所有值

score = { 'july':89, 'candy':98, 'test':100 }
print(score)
print(score['july'])
print(score['candy'])
score['linye'] = 88   #add
print(score)

if 'linye' in score:
    print("linye:",score['linye'])
else:
    print("linye not exist")

score.pop('linye')
print(score)

if 'linye' in score:
    print("linye:",score['linye'])
else:
    print("linye not exist")

#以列表返回一个字典所有的键
score.keys()
print(score.keys())

#http://www.runoob.com/python/python-dictionary.html
##############################################################

#############################函数#############################
n=abs(-3)
print(n)

m=max(1, 2, 9, -1)
print(m)

m=min(1, 2, 9, -1)
print(m)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

n = my_abs(-1.99)
print(n)
n = my_abs(3.2)
print(n)
##############################################################

########################默认参数函数##########################
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

n = power(5)
print(n)

n = power(5,3)
print(n)
##############################################################

########################可变参数函数##########################
def calc(*numbers):     #可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

n = calc(1, 2, 3)
print(n)

nums = [1, 2, 3]
n = calc(*nums)     #可变参数传入
print(n)
##############################################################

###########################生成器#############################
#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
L = list(range(1, 11))
print(L)

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(0, 10):
    L.append(x * x)
print(L)

#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L = [x * x for x in range(10)]
print(L)

#可以添加条件再次过滤，
L = [x * x for x in range(10) if x % 2 == 0]
print(L)
##############################################################

###########################生成器#############################
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

g = (x * x for x in range(10))
print(g)
print(next(g))

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(5)

#要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(5))

def triangles(max):
    n,a,b = 0,0,1
    Lold = []
    Lnew = [1]
    while n < max:
        print(Lnew)
        a, b = b, a + b
        Lnew.insert(n,b)
        n = n + 1
    return 'done'

triangles(5)

def triangles2(max):
    n = 0
    N = [1]
    while n < max:
        print(N)
        #yield N
        N.append(0)
        N = [N[n-1] + N[n] for n in range(len(N))]
        n = n + 1
    return 'done'

triangles2(5)
##############################################################

#########################map reduce###########################
def normalize(L):
    return str.capitalize(L)

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def prod(x, y):
    return x * y

print('3 * 5 * 7 * 9 =', reduce(prod, ([3, 5, 7, 9])))
##############################################################

############################排序##############################
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))   #将内部的值ads后再排序，升序
print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True)) #降序

from operator import itemgetter

students = [('Bob', 75, 1), ('Adam', 92, 3), ('Bart', 66, 2), ('Lisa', 88, 4)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1)))
print(sorted(students, key=itemgetter(1), reverse=True))
print(sorted(students, key=itemgetter(2)))
##############################################################

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    h = sorted(environ.items())
    for k, v in h:
        print(k, '=', repr(v))

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

with make_server('0.0.0.0', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()



import os, shutil

