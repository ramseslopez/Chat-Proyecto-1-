import socket
import threading
import sys
import pickle

class Cliente:


    def __init__(self, IP, puerto): 
        """
        Metodo que crea un instancia de la clase donde iniciliza un socket
        y la direccion del cliente
        """
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.direccion_cliente = (str(IP), int(puerto))


    def obtener_socket(self):
        """
        Metodo para obtener el socket definido
        """
        return self.mi_socket

    def asignar_socket(self, socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        """
        Método para asignar al cliente una nuevo socket
        """
        self.cerrar_socket()
        self.mi_socket = socket

    def obtener_direccion(self):
        """
        Metodo para obtener la direccion del cliente que se va a conectar con
        el servidor.
        """
        return self.direccion_cliente

    def asignar_direccion(self, IP, puerto):
        """
        Método para asignar al cliente una direccion con la cual se va a 
        conectar con el servidor.
        """
        self.IP = str(IP)
        self.puerto = int(puerto)
        self.direccion_cliente = (self.IP,self.puerto)


    def manejar_mensajes(self):
        """
        Metodo que se encarga de asignar a un hilo de ejecucion la tarea de 
        recibir los mensajes.
        """
        mensaje_recibido = threading.Thread(target = self.recibir_mensaje)
        mensaje_recibido.setDaemon(True)
        mensaje_recibido.start()


    def enviar_mensajes(self):
        """
        Metodo que se encarga de enviar el mensaje a todos los clientes 
        conectados.
        """
        print("Dame tu nombre de usuario: ")
        nombre_cliente = str(input())
        self.asignar_estado()
        print("Escribe tus mensajes")
        while True:
            entrada = str(input())
            if entrada != "salir":
                self.enviar_mensaje(nombre_cliente, entrada)
            else:
                self.cerrar_socket()
                sys.exit()
                

    def recibir_mensaje(self):
        """
        Metodo que se encarga de aceptar los mensajes de otros clientes
        conectados
        """
        while True:
            try:
                respuesta = self.mi_socket.recv(1024)
                if respuesta:
                    print(pickle.loads(respuesta))
            except:
                pass


    def enviar_mensaje(self, nombre_cliente, mensaje):
        """
        Se encarga de enviar los mensajes a un usuario en específico
        """
        try:
            self.mi_socket.send(pickle.dumps("["+ nombre_cliente +"]: " + mensaje))
        except:
            print("Ocurrió un error al enviar el mensaje")

    def ejecutar_cliente(self):
        """
        Metodo que se encarga de conectar al cliente con el servidor
        """
        self.obtener_socket().connect(self.direccion_cliente)
        self.manejar_mensajes()
        self.enviar_mensajes()

    def asignar_estado(self):
        print("Elige un estado: ")
        print("1. ACTIVE")
        print("2. AWAY")
        print("3. BUSY")
        opcion = str(input("opcion:  "))
        switcher = {
            '1' : 'ACTIVE',
            '2' : 'AWAY',
            '3' : 'BUSY'
        }
        self.estado = switcher.get(opcion, "Opcion invalida")
        return self.estado


#a=sys.argv[1]
#b=sys.argv[2]

#cliente = Cliente(a,b)
#cliente.ejecutar_cliente()
