import socket

SERVER_PORT = 8080
USER_LISTEN = 4

s1 = None
s2 = None

_s = None

try:
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.bind(('0.0.0.0', SERVER_PORT))
    _socket.listen(USER_LISTEN)
    _s = _socket
except Exception as e:
    print(f'Ocorreu um erro ao criar socket tcp: {e}')
finally:
    if _s != None:
        _s = _socket
        print(_s)
        _s.close