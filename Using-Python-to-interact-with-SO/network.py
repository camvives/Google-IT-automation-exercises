"""
Verificación de conexiones del equipo
"""
import socket
import requests

def check_localhost():
    '''Verifica que el equipo esté conectado a la red local'''

    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_connectivity():
    '''Verifica que el equipo esté conectado a internet'''

    request = requests.get("http://google.com")
    return request.status_code == 200

print(check_localhost())
print(check_connectivity())
