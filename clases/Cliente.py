import socket
import threading
import sys
import pickle

class Cliente:

    def __init__(self, IP = "localhost", puerto = 5000):
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mi_socket.connect( (IP, puerto) )
        mensaje_recibido = threading.Thread(target = self.recibir_mensaje)
        mensaje_recibido.daemon = True
        mensaje_recibido.start()
        while True:
            entrada = input('(^▽^) ')
            if entrada != "salir":
                self.enviar_mensaje(entrada)
            else:
                self.mi_socket.close()
                sys.exit()
                

    def recibir_mensaje(self):
        while True:
            try:
                respuesta = self.mi_socket.recv(1024)
                if respuesta:
                    print(pickle.loads(respuesta))
            except:
                pass

    def enviar_mensaje(self, mensaje):
        try:
            self.mi_socket.send(pickle.dumps(mensaje))
        except:
            print("Ocurrió un error al enviar el mensaje")


cliente = Cliente()
