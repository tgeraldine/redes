import json

from datetime import datetime

from enum import Enum

class Protocol(Enum):
    GET = 1
    POST = 2
    SYNC = 3

    @staticmethod
    def get_protocol(value: int):
        return [Protocol.GET, Protocol.POST, Protocol.SYNC][value]

class Message:
    def __init__(self, message: str, timestamp: str = datetime.now().strftime("%H:%M:%S")) -> None:
        self.__message = message
        self.__timestamp = timestamp

    @staticmethod
    def fromJson(element: object) -> 'Message':
        return Message(element['__message'], element['__timestamp'])
    
    def toJson(self) -> object:
        return {
            "message": self.__message,
            "timestamp": self.__timestamp
        }

class Payload:
    def __init__(self, protocol: Protocol, address: str, message: Message = Message('None')) -> None:
        self.__protocol = protocol
        self.__address = address
        self.__message = message

    @staticmethod
    def fromJson(element: json) -> 'Payload':
        protocol = Protocol.get_protocol(element['protocol'])
        message = Message.fromJson(element['message'])

        return Payload(protocol, element['address'], message)

    def toJson(self) -> object:
        return {
            "protocol": self.__protocol.value,
            "address": self.__address,
            "message": self.__message.toJson()
            }