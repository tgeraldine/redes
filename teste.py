b1: bytes = bytes()
b1 = b1 + 'hello'.encode()
b1 = b1 + ' world. how are you?'.encode()


print(b1.__sizeof__())