import socket
import threading
import sys
import pickle


class Servidor:

    
    def __init__(self, IP = "localhost", puerto = 5000):
        self.conexiones = []
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mi_socket.bind((IP, puerto))
        self.mi_socket.listen(10)
        self.mi_socket.setblocking(False)
        hilo_1 = threading.Thread(target = self.aceptar_conexiones)
        hilo_2 = threading.Thread(target = self.manejo)
        hilo_1.daemon = True
        hilo_1.start()
        hilo_2.daemon = True
        hilo_2.start()
        try:
            while True:
                print("Esperando conexión ...")
                mensaje = input("")
                if mensaje == "salir":
                    break
            self.mi_socket.close()
            sys.exit()
        except:
            pass

    def mensajes(self, mensaje, cliente):
        for c in self.conexiones:
            try:
                if c != cliente:
                    c.send(mensaje)
            except:
                self.conexiones.remove(c)


    def aceptar_conexiones(self):
        while True:
            try:
                connection, addr = self.mi_socket.accept()
                connection.setblocking(False)
                self.conexiones.append(connection)
                print(str(addr[0])+ ": " + str(addr[1]) + " connected")
            except:
                pass
            
    def manejo(self):
        while True:
            if len(self.conexiones) > 0:
                for clt in self.conexiones:
                    try:
                        datos = clt.recv(1024)
                        if datos:
                            self.mensajes(datos, clt)
                    except:
                        pass
        

servidor = Servidor()