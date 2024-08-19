import json

from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class Protocol(Enum):
    GET = 1
    POST = 2
    SYNC = 3
    KNOW = 4

    @staticmethod
    def get_protocol(value: int):
        return [Protocol.GET, Protocol.POST, Protocol.SYNC][value]

class Message(ABC):
    @staticmethod
    def fromJson(_type: Protocol, _json: json) -> 'Message':
        match _type:
            case Protocol.GET:
                return GetMessage(_json['message'])
            case Protocol.POST:
                return PostMessage(_json['message'], _json['timestamp'])
            case Protocol.SYNC:
                return SyncMessage(_json['message'])
            case Protocol.KNOW:
                return KnowMessage(_json['message'])
    
    @abstractmethod
    def toJson(self) -> object:
        return {
            "message": self.__message,
            "timestamp": self.__timestamp
        }

class GetMessage(Message):
    def __init__(self, message: int) -> None:
        self.__message = message

class PostMessage(Message):
    def __init__(self, message: str, timestamp: str = datetime.now().strftime("%H:%M:%S")) -> None:
        self.__message = message
        self.__timestamp = timestamp

class SyncMessage(Message):
    def __init__(self, message: str) -> None:
        self.__message = message

class KnowMessage(Message):
    def __init__(self, message: int) -> None:
        self.__message = message

class Payload:
    def __init__(self, protocol: Protocol, address: str, message: Message = Message('None')) -> None:
        self.__protocol = protocol
        self.__message = message

    @staticmethod
    def fromJson(element: json) -> 'Payload':
        protocol = Protocol.get_protocol(element['protocol'])
        message = Message.fromJson(element['message'])

        return Payload(protocol, element['address'], message)

    def toJson(self) -> object:
        return {
            "protocol": self.__protocol.value,
            "message": self.__message.toJson()
            }
    
    def get_message():