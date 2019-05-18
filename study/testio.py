import os

print("start")

print(os.name)

print(os.path.abspath('.'))

#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('D:\Python\\first', 'testdir')

if os.path.isdir('D:\\Python\\testdir'):
    # 删掉一个目录:
    os.rmdir('D:\\Python\\testdir')
else:
    # 然后创建一个目录:
    os.mkdir('D:\\Python\\testdir')


fd = open('D:\\Python\\testio','w')
fd.write('Hello, world!')
fd.close()

#在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：

# try:
#     f = open('/path/to/file', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()
#
# #写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：
#
# with open('/path/to/file', 'r') as f:
#     f.read()


# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello World!")
#     #异步调用asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print("Hello Again!")
#
# #获取EventLoop
# loop = asyncio.get_event_loop()
# #执行 coroutine
# loop.run_until_complete(hello())
# loop.close()

#说明：hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

import asyncio

@asyncio.coroutine
def wget(host):
    print("wget %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    #Ignore the body,close the socket
        writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()