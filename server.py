import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostbyname()
port = 444
#host=192.168.18.4
serversocket.bind(("192.168.18.4", port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("Received connection from " % str(address))
    message = 'Hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()

