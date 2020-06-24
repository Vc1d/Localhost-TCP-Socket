import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 1024
ENCODING = 'utf-8'

client.connect((HOST, PORT))

username = input("Enter your username\n")


def receive():
    while True:
        try:
            msg = client.recv(1024).decode(ENCODING)
            if msg == 'USERNAME':
                client.send(username.encode(ENCODING))
            else:
                print(msg)
        except:
            print("Error")
            client.close()
            break


def inputname():
    while True:
        msg = f'{username}: {input("")}'
        client.send(msg.encode(ENCODING))


rcv_thread = threading.Thread(target=receive)
rcv_thread.start()

input_thread = threading.Thread(target=inputname)
input_thread.start()
