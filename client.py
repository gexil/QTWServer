# -*- coding: iso-8859-1 -*-
"""
Created on Thu Apr 12 01:14:51 2018

@author: emmanuel
"""

 
import socket
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
msg = "This is from Client"
client.sendall(bytes(msg.encode("UTF-8")))
while True:
  in_data =  client.recv(1024)
  print("From Server :" ,in_data.decode())
  out_data = input()
  client.sendall(bytes(out_data.encode("UTF-8")))
  if out_data=='bye':
      break
client.close()
