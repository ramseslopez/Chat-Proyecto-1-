import socket
import threading
import sys
import pickle


class Servidor:

    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexiones = []

    def __init__(self, IP, puerto):
        """
        Metodo que crea un instancia de la clase donde iniciliza un 
        socket, la direccion del cliente y la lista de conexiones
        """
        self.obtener_conexiones()
        self.obtener_socket()
        self.direccion = (str(IP), int(puerto))

    def obtener_socket(self):
        """
        Metodo para obtener el socket definido.
        """
        return self.mi_socket

    def asignar_socket(self, socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        """
        Metodo para asignar al cliente una nuevo socket
        """
        self.mi_socket.close()
        self.mi_socket = socket

    def obtener_num_conexiones(self):
        """
        Metodo para obtener el numero de conexiones del chat.
        """
        return len(self.conexiones)

    def obtener_conexiones(self):
        """
        Metodo para obtener las conexiones
        """
        return self.conexiones

    def obtener_direccion(self):
        """
        Metodo para obtener la direccion con la cual se ejecutara 
        el servidor.
        """
        return self.direccion

    def asignar_direccion(self, IP, puerto):
        """
        Metodo para asignar al servidor una direccion con la cual se va a 
        ejecutar el servidor.
        """
        self.IP = str(IP)
        self.puerto = int(puerto)
        self.direccion = (self.IP, self.puerto)
       
    def manejar_conexiones(self):
        """
        Metodo que se encarga de asignar a hilos de ejecucion las tareas del
        manejo y envio de los mensajes.
        """
        aceptar_conn = threading.Thread(target = self.aceptar_conexiones)
        manejo = threading.Thread(target = self.manejo)
        aceptar_conn.setDaemon(True)
        aceptar_conn.start()
        manejo.setDaemon(True)
        manejo.start()


    def establecer_conexion(self):
        """
        Se encarga de establecer la conexion y esperar a que los clientes se
        conecten para interactuar entre ellos
        """
        try:
            while True:
                print("Esperando conexion ...")
                mensaje = input("")
                if mensaje == "salir":
                    break
            self.mi_socket.close()
            sys.exit()
        except:
            pass


    def mensajes(self, mensaje, cliente):
        """
        Metodo que se encarga de enviar los mensajes a todos los clientes
        conectados.
        """
        for conexion in self.conexiones:
            try:
                if conexion != cliente:
                    conexion.send(mensaje)
            except:
                self.conexiones.remove(conexion)
                print(cliente)


    def aceptar_conexiones(self):
        """
        Metodo que se encarga de aceptar la conexion de los clientes.
        """
        while True:
            try:
                connection, addr = self.mi_socket.accept()
                connection.setblocking(False)
                self.conexiones.append(connection)
                print(str(addr[0])+ ": " + str(addr[1]) + " connected")
            except:
                pass
                
            
    def manejo(self):
        """
        Metodo que se encarga del manejo de los clientes y los mensajes 
        dentro del chat.
        """
        while True:
            if self.obtener_num_conexiones() > 0:
                for clt in self.conexiones:
                    try:
                        datos = clt.recv(1024)
                        if datos:
                            self.mensajes(datos, clt)
                    except:
                        pass

    def ejecutar_servidor(self):
        """
        Metodo que se encarga de ejecutar al servidor.
        """
        self.mi_socket.bind(self.direccion)
        self.mi_socket.listen(500)
        self.mi_socket.setblocking(False)
        self.manejar_conexiones()
        self.establecer_conexion()
        

#servidor = Servidor(str(sys.argv[1]),int(sys.argv[2]))
#servidor.ejecutar_servidor()
