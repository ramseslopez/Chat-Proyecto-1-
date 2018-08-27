import socket
import threading

class Cliente:

    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def enviarMensaje(self, direccion):
        while True:
            self.mi_socket.send(bytes(input(""), 'utf-8'))

    def __init__(self, direccion):
        self.mi_socket.connect( (direccion, 10000) )
        hilo = threading.Thread(target = enviarMensaje)
        hilo.setDaemon(True)
        hilo.start()
        while True:
            respuesta = mi_socket.recv(1024)
            if respuesta == None:
                break