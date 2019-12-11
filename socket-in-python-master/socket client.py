import time
import random
import socket
HOST = '127.0.0.1'
PORT = 5552

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 456)) #指定出去的port
s.connect((HOST, PORT))

while True:
    inp=random.choice('0123456789')
    s.send(inp.encode('utf-8'))
    print(inp)
    data = s.recv(1024)
    print ("receive from ser :",data.decode('utf-8'))
    time.sleep(0.7)
s.close()