import threading
import socket

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 1024
ENCODING = 'utf-8'

SERVER.bind((HOST, PORT))
SERVER.listen()

clients = []
usernames = []


def sendall(msg):
    for client in clients:
        client.send(msg)


def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            sendall(msg)

        except:
            index = clients.index(client)
            clients.remove(client)
            username = usernames[index]
            usernames.remove(username)
            sendall(f'{username} left the chat...'.encode(ENCODING))
            break


def receive():
    while True:
        client, address = SERVER.accept()
        print(f'{str(address)} has connected')
        client.send('USERNAME'.encode(ENCODING))
        username = client.recv(64).decode(ENCODING)
        usernames.append(username)
        clients.append(client)

        sendall(f'{username} has joined the chat... '.encode(ENCODING))
        client.send("Connected".encode(ENCODING))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print(f'Server is listening on {HOST}')
receive()
