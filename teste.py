import socket 

def obter_ip_local():
    try:
        # Obtém o nome do host local
        hostname = socket.gethostname()
        # Obtém a lista de endereços IP do host local
        ip_list = socket.gethostbyname_ex(hostname)[2]
        # Retorna todos os IPs locais encontrados
        return ip_list
    except Exception as e:
        return f'Erro: {e}'
    
print(obter_ip_local())