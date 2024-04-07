from socket import *
import commons
import time

# first run this file!!!!

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', commons.server_port))

print('receiver is on...')

hidden_message = ''
nice_message= ''

for i in range(commons.message_len * 8):
    start = time.time()
    data, addr = server_socket.recvfrom(1024)
    finish = time.time()
    receiving_time = finish - start

    if not data:
        print('data finished!!!')
        break

    nice_message += data.decode()

    if receiving_time > commons.delta / 2:
        hidden_message += '1'
    else:
        hidden_message += '0'

print('nice_message: ')
for i in range(0, len(nice_message), 8):
    character = chr(int(nice_message[i:i + 8], 2))
    print(character, end='')

print()
print('hidden_message: ')
for i in range(0, len(hidden_message), 8):
    character = chr(int(hidden_message[i:i + 8], 2))
    print(character, end='')





