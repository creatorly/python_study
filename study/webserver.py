import socket
import requests

from a import normalize

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


HOST, PORT = '', 8888
#r = requests.get('http://192.168.1.50:80/goip_get_status.html?username=root&password=root')

"""
search = '['
num_a = str(r.json)
start = num_a.index(search) + 1

print(num_a[start:start+3])
"""

r = requests.get('http://192.168.0.52:18080/esps2/server/dev_info.json?dev=532')
print(r.text)
print(r.status_code)

r = requests.get('http://192.168.0.52:18080/esps2/server/slot_info.json?slot=532.01')
print(r.text)
print(r.status_code)

r = requests.get('http://192.168.0.52:18080/esps2/server/dev_info.json?dev=sp256')
print(r.text)
print(r.status_code)

r = requests.get('http://192.168.0.52:18080/esps2/server/slot_info.json?slot=sp256.002')
print(r.text)
print(r.status_code)

r = requests.post('http://192.168.0.52:18080/esps2/server/sim_bind.json?goip_slot=532.01&sim_slot=sp256.002')
print(r.text)
print(r.status_code)

r = requests.post('http://192.168.0.52:18080/esps2/server/sim_unbind.json?goip_slot=532.01&sim_slot=sp256.002')
print(r.text)
print(r.status_code)

"""
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode()
    print(request)

    http_response = ""HTTP/1.1 200 OK
Hello, World!
""
    #client_connection.sendto(('[%s] %s' % (ctime(), http_response)).encode(), client_address)
    #client_connection.sendall(bytes(http_response))
    client_connection.sendall(bytes('你好', encoding='utf-8'))
    client_connection.close()
"""