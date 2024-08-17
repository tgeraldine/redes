from enum import Enum

class Protocol(Enum):
    GET = 1
    POST = 2
    LOGIN = 3
    REGISTER = 4

class PostData:
    def __init__(self, user: str, data: str, timestamp: str) -> None:
        self.user = user
        self.data = data
        self.timestamp = timestamp

    def toJSON(self):
        return {
            "user": self.user,
            "data": self.data,
            "timestamp": self.timestamp
            }
        
class GetData:
    def __init__(self, data: list[PostData]) -> None:
        self.data = data

    def toJSON(self):
        return {"data": self.data}

class Payload:
    def __init__(self, protocol: Protocol, data: GetData | PostData) -> None:
        self.protocol = protocol
        self.data = data

    def toJSON(self):
        return {
            "protocol": self.protocol.value,
            "data": self.data.toJSON()
            }