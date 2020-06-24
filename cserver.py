# Import the needed modules
import threading
import socket

# Define the constants
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 1024
ENCODING = 'utf-8'

# use the bind function to start the server and make it listen for clients
SERVER.bind((HOST, PORT))
SERVER.listen()

# make two lists of the client name and the username the user inputs
clients = []
usernames = []

# Define a function that sends the same message to every client connected
def sendall(msg):
    for client in clients:
        client.send(msg)

# Define a function that sends a message to all clients when a user leaves and removes the client and username from the clients and usernames list
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

# This is the main function that listens for clients and accepts them into the server
def receive():
    while True:
        client, address = SERVER.accept()
        print(f'{str(address)} has connected')
        client.send('USERNAME'.encode(ENCODING))
        username = client.recv(64).decode(ENCODING)
        # Append the username and client to the usernames and clients list
        usernames.append(username)
        clients.append(client)
        
        # Send a message to all clients letting them know that another client has joined
        sendall(f'{username} has joined the chat... '.encode(ENCODING))
        client.send("Connected".encode(ENCODING))
        
        # threading because the main function has a while loop
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

# Check if the Server is running
print(f'Server is listening on {HOST}')
# run main
receive()
