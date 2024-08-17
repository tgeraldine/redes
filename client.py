import json

import socket

from protocol import *

from datetime import datetime

DATA_PAYLOAD = 4096

bufferMessages = []

loopCondition = True

def start():
    serverAddress = input('Server IP: ')
    serverPort = int(input('Server PORT: '))
    clientNick = input('Nickname: ')

    while loopCondition:
        printBufferMessages()

        client(nickname=clientNick, server_address=(serverAddress, serverPort))

        break

def printBufferMessages():
    for message in bufferMessages:
        print(f'{message['client']}: {message['message']}\n')


def client(nickname, server_address): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.connect(server_address)

    try: 
        message = processClientMessage(nickname=nickname, message=input('> '))

        sock.sendall(message)

        serverMessage = waitServerResponse(sock=sock)

        processServerMessage(serverMessage)
    finally: 
        sock.close()

def processClientMessage(nickname, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    data = PostData(nickname, str(message), timestamp)
    payload = Payload(Protocol.POST, data)

    return json.dumps(payload.toJSON()).encode()

def processServerMessage(message):
    decodedMessage = message.decode()
    jsonMessage = json.loads(decodedMessage)
    bufferMessages.append(jsonMessage)
    print(jsonMessage)

def waitServerResponse(sock: socket):
    data = None

    while data == None:
        data = sock.recv(DATA_PAYLOAD)

    return data

start()