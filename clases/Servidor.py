import socket
import threading
import sys
import pickle


class Servidor:

   
    def __init__(self, IP = "localhost", puerto = 5000):
        self.conexiones = []
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mi_socket.bind((IP, puerto))
        self.mi_socket.listen(500)
        self.mi_socket.setblocking(False)
        self.asignar_hilos()
        self.establecer_conexion()

        
    def asignar_hilos(self):
        """Se encarga de a los hilos de ejecucion las tareas del manejo y
        envío de los mensajes"""
        hilo_1 = threading.Thread(target = self.aceptar_conexiones)
        hilo_2 = threading.Thread(target = self.manejo)
        hilo_1.setDaemon(True)
        hilo_1.start()
        hilo_2.setDaemon(True)
        hilo_2.start()


    def establecer_conexion(self):
        """Se encarga de establecer la conexión y esperar a que los clientes se
        conecten para interactuar entre ellos"""
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
        """Se encarga de enviar los mensajes a todos los clientes"""
        for c in self.conexiones:
            try:
                if c != cliente:
                    c.send(mensaje)
            except:
                self.conexiones.remove(c)


    def aceptar_conexiones(self):
        """Se encarga de aceptar la conexión de los clientes y mostar la conexión"""
        while True:
            try:
                connection, addr = self.mi_socket.accept()
                connection.setblocking(False)
                self.conexiones.append(connection)
                print(str(addr[0])+ ": " + str(addr[1]) + " connected")
            except:
                pass
                
            
    def manejo(self):
        """Se encarga del manejo de los clientes y los mensajes dentro del chat"""
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