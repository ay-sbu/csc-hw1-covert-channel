from socket import *
import commons
import time
import threading

# first run ayreceiver.py!!!!!!

hidden_message =    "-I hack you!"
nice_message =      "-I love you!"

def send_message():
    global hidden_message, nice_message, client_socket

    hidden_message = ''.join(format(ord(i), '08b') for i in hidden_message)
    nice_message = ''.join(format(ord(i), '08b') for i in nice_message)

    for i in range(len(hidden_message)):
        if hidden_message[i] == '1':
            time.sleep(commons.delta)
        client_socket.sendall(nice_message[i].encode())

# main
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.connect((commons.server_ip, commons.server_port))

start = time.time()

send_message()

finish = time.time()
sending_time = finish - start

speed = len(hidden_message) / sending_time
print('speed bit/second: ', speed)

client_socket.close()