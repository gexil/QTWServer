# -*- coding: iso-8859-1 -*-
"""
Created on Thu Apr 12 00:08:11 2018

@author: emmanuel
"""

 
import socket
from threading import Thread

from event import Event
from select import select

class TCPServerChild(Thread):
    """
    TCPServerChild: class for use with TCPServer. Uses the Thread subclass.
    
    @socket: client tuple in the form of (socket, client_addr)
    @run: this function should be overwritten with client-handling code
    """
    
    def __init__(self, socket):
        Thread.__init__(self)
        self.stop = False
        self.socket, self.address = socket
        self.evt_clientConnected = Event()
        self.evt_clientDisconnected = Event()
        self.evt_clientReceive = Event()
                
        
    def recv(self, nbytes=1024, timeout=None):
        """
        recv: read n bytes from socket. optional timeout
        @bytes: max bytes to read from the socket
        @timeout: timeout for the read procedure in seconds
        """

        if timeout:
            readable, writable, errored = select([self.socket, ], [], [], timeout)
            if self.socket in readable:
                try:
                    data = self.socket.recv(nbytes)
                except:
                    data = None
                return data
            else:
                return None
        else:
            try:
                data = self.socket.recv(nbytes)
            except:
                data = None
            return data

    def send(self, data, timeout=None):
        """
        send: write data to the socket. optional timeout
        @data: data (str) to send to the socket
        @timeout: timeout for the send procedure in seconds
        """

        if timeout:
            readable, writable, errored = select([self.socket, ], [], [], timeout)
            if self.socket in writable:
                return self.socket.send(data)
            else:
                return None                
        else:
            return self.socket.send(data)
    
    
    def close(self):
        """ overwrite with initial server function """
        self.stop = True

    def run(self):
        self.evt_clientConnected(self, "New connection added from "+str(self.address))
        while not self.stop:
            data = self.recv()
            if(not (data is None)):
                print data
                self.send("ACK : "+data)
                self.evt_clientReceive(self, "from client "+str(self.address)+" : "+data)
            else:
                break
        self.socket.close()
        self.evt_clientDisconnected(self, "Client at "+str(self.address)+" disconnected...")

class TCPServer(Thread):
    """
    TCPServer class: creates a listening socket and spawns threads for every connected client
    
    @bind_socket: socket tuple in the form (ipaddr, socket) to bind to
    @callback: class with subclass of TCPServerChild to handle each client connection
    @max_connections: maximum number of concurrend client connections
    """
    
    thread_pool = []
    
    def __init__(self, bind_socket, max_connections = 10):  
        Thread.__init__(self)
        self.bind_socket = bind_socket
        self.max_connections = max_connections
        self.numberOfConnexion = 0
        self.evt_server_clientConnected = Event()
        self.evt_server_clientDisconnected = Event()
        self.evt_server_clientReceive = Event()
        self.Active = True
    
    def stop(self):
        self.Active = False
        
    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.bind_socket)
        self.sock.listen(self.max_connections)
        
        while self.Active:
            try:
                readable, writable, errored = select([self.sock, ], [], [], 1)
                if self.sock in readable:
                    child = TCPServerChild(self.sock.accept())
                    child.evt_clientConnected += self.onClientConnected
                    child.evt_clientDisconnected += self.onClientDiconnected
                    child.evt_clientReceive += self.onClientReceive
                    self.thread_pool.append(child)
                    self.thread_pool[-1].start()        
                    
                # clean up
                for thread in self.thread_pool[:]:
                    if not thread.is_alive():
                        self.thread_pool.remove(thread)
                self.numberOfConnexion = len(self.thread_pool)
                    
                        
            except KeyboardInterrupt:
                break
                pass
    
            #print len(self.thread_pool)
        for thread in self.thread_pool[:]:
                    thread.close()        
        self.sock.close()
        print "Bye !"
    
    def onClientConnected(self, sender, message):
        self.evt_server_clientConnected(self, message)
    
    def onClientDiconnected(self, sender, message):
        self.evt_server_clientDisconnected(self, message)
    
    def onClientReceive(self, sender, message):
        self.evt_server_clientReceive(self, message)