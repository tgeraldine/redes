import socket

from lib.protocol import *

PAYLOAD_SIZE = 1028
SERVER_PORT = 8080

class ClientSocket:
    __host_ip = None
    __server_ip = None

    def __init__(self) -> None:
        print('Creating socket started...')

        self.__host_ip = get_host_ip()

        self.__server_ip = self.__get_server_ip()

    def get_messages(self):
        pass

    def send_message(self, message: str):
        pass

    def __get_server_ip(self) -> None:
        print('Serching for server...')

        try:
            _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            _socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

            payload = Payload(Protocol.SYNC, SyncMessage('Are you the server?'))

            _socket.send(('<broadcast>', SERVER_PORT), payload)

            return self.__recv_sync(_socket).message.get_content()
        except Exception as e:
            print(f'Exceção ao tentar enviar broadcast. |_{e}')

    def __recv_multiple(self, _socket: socket):
        try:
            knowledge: Payload = self.__recv_knowledge(_socket)

            bytes_message: bytes = bytes()

            while knowledge.message.message != bytes_message.__sizeof__():
                bytes_message = _socket.recv(PAYLOAD_SIZE)
        except Exception as e:
            Exception(f'Exception at __recv_multiple. |_{e}')

    def __recv_unique(_socket: socket) -> Payload:
        try:
            byte_message: bytes = _socket.recv(PAYLOAD_SIZE)

            string_message: str = byte_message.decode()

            json_message: json = json.loads(string_message)

            return Payload.fromJson(json_message)
        except Exception as e:
            raise Exception(f'Exception at __recv_unique. |_{e}')
        
class ServerSocket:
    USER_LISTEN = 4

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
            _socket.listen(self.USER_LISTEN)
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
    