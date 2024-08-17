import socket

from lib.protocol import *

SERVER_PORT = 8080
USER_LISTEN = 4

class ClientSocket:
    __host_ip = None
    __server_ip = None

    def __init__(self) -> None:
        print('Creating socket started...')

        self.__host_ip = get_host_ip()

    def __get_server_ip() -> None:
        print('Serching for server...')

        try:
            _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            _socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

            address = _socket.getsockname()[0]
            payload = Payload(protocol=Protocol.SYNC, address=address)

            _socket.send(('<broadcast>', SERVER_PORT), payload)
        except Exception as e:
            print(f'Exceção ao tentar enviar broadcast: {e}')

    def __wait_response(sock: socket):
        

        
class ServerSocket:
    __tcp_socket = None
    __udp_socket = None
    __host_address = None

    def __init__(self):
        print('Server socket started...')

        self.__host_address = get_host_ip()

        self.__create_tcp_socket()
        self.__create_udp_socket()

    def __create_tcp_socket(self):
        _socket = None

        try:
            _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _socket.bind((self.__host_address, SERVER_PORT))
            _socket.listen(USER_LISTEN)
        except Exception as e:
            print(f'Exceção ao criar socket TCP: {e}')
        finally:
            if _socket != None:
                self.__tcp_socket = _socket

    def __create_udp_socket(self):
        _socket = None

        try:
            _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            _socket.bind((self.__host_address, SERVER_PORT))
        except Exception as e:
            print(f'Exceção ao criar socket UDP: {e}')
        finally:
            if _socket != None:
                self.__udp_socket = _socket

    def __handle_tcp_client():
        print('TCP client...')

    def __handle_udp_client():
        print('UDP client...')

def get_host_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as _socket:
        _socket.connect('255.255.255.255', 0)

        ip_address = _socket.getsockname()

        _socket.close()

        return ip_address[0]
    