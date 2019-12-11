import socket

HOST = '127.0.0.1'
PORT = 5552

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print (HOST, PORT)
print ('wait')
conn, addr = s.accept()

print ('Connected by ', addr)
while True:
    data = conn.recv(1024)
    print (data.decode('utf-8'))
    mesgg="get it:"
    mesgg+=data.decode('utf-8')
    conn.send(mesgg.encode('utf-8'))
conn.close()

