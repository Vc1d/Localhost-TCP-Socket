# import the needed modules
import threading
import socket

# create a new socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the constants
HOST = '127.0.0.1'    # localhost
PORT = 1024           # TCP Port I used, but you can use any port that doesn't server a great purpose
ENCODING = 'utf-8'    # Encoding I used. You can use pretty much any encoding such as ascii, utf-16, etc.

# Connect the client to the server by localhost and the TCP port
client.connect((HOST, PORT))

# Make the user input a username
username = input("Enter your username\n")

# Define a function to recieve messages
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

# Define a function to send messages to other clients
def inputname():
    while True:
        msg = f'{username}: {input("")}'
        client.send(msg.encode(ENCODING))

# Set up threading so you can receive and send at the same time (while loop doesn't allow anything else to run without it finishing first)
rcv_thread = threading.Thread(target=receive)
rcv_thread.start()

input_thread = threading.Thread(target=inputname)
input_thread.start()
