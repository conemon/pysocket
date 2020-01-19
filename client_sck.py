import socket
import os
import subprocess
import time

class client:

    def __init__(self, host, port):
        self.sck = None
        self.host = host
        self.port = port
        self.retry_limit = 2 #default value, set this limit with setRetryLimit() method
        self.retry_count = 0
        print("Client object has been created!")

    def setRetryLimit(self, retry_lim):
        self.retry_limit = retry_lim

    def create_socket(self):
        self.sck = socket.socket()

    def connect(self):
        try:
            self.create_socket()
            self.sck.connect((self.host, self.port))
            print(f"connected to the server {self.host} on port {self.port} successfully")
        except Exception as e:
            print(f"OOPS Something gone wrong! {e}. Retrying...")
            if self.retry_count < self.retry_limit:
                self.retry_count += 1
                self.connect()
                time.sleep(3)
            else:
                print("Retry limit has exceeded!...closing")
                self.sck.close()
                return

    def receiveData(self):
        while True:
            data = self.sck.recv(1024)
            data_decoded = data.decode('utf-8')
            print(data_decoded)


client1 = client("192.168.1.17", 9999)
client1.setRetryLimit(6)
client1.connect()
client1.receiveData()

