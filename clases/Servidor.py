import socket
import threading


class Servidor:

    mi_socket = socket.socket()
    conexiones = []
    
    def __init__(self):
        self.mi_socket.bind(('0.0.0.0', 10000))
        self.mi_socket.listen(1)

    def manejo(self, conexion, direccion):
        while True:
            peticion = conexion.recv(1024)
            for conexion in self.conexiones:
                conexion.send(bytes(peticion))
            if peticion == None:
                break

    def ejecutar(self):
        conexion, direccion = self.mi_socket.accept()
        hilo = threading.Thread(target = manejo, args = (conexion,direccion))
        hilo.setDaemon(True)
        hilo.start()
        self.conexiones.append(conexion)
        print(slef.conexiones)

