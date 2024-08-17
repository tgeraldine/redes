import json

import socket
import threading

DATA_PAYLOAD = 4096

clientBuffer = []

messageBuffer = []

def server():
    server_address = (obter_ip_local(), 8080)

    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(server_address)

    sock.listen(4)

    while True:
        client, address = sock.accept()

        clientThread = threading.Thread(target=handleClient, args=(client, address))
        clientThread.start()
        break

def handleClient(client, address):
    addClient(address)

    payload = client.recv(DATA_PAYLOAD)

    if payload:
            processClientMessage(payload)

            client.send(json.dumps(messageBuffer).encode())

            client.close()

def addClient(addr):
    if addr not in clientBuffer:
        clientBuffer.append(addr)

def processClientMessage(message):
    _message = message.decode()
    _json = json.loads(_message)

    messageBuffer.append(_json)
    print(_json)


def obter_ip_local():
    try:
        hostname = socket.gethostname()

        ip_list = socket.gethostbyname_ex(hostname)[2]

        return ip_list[0]
    except Exception as e:
        return f'Erro: {e}'

server()