from chat.clases import Servidor
from chat.clases import Cliente
import unittest
import socket
import random

class TestServidor(unittest.TestCase):

    def test_ObtenerDireccion(self):
        self.servidor = Servidor.Servidor("xxxx.xxxx.xxxx.xxxx", 0)
        self.servidor.asignar_direccion("localhost", 55)
        self.assertEqual(("localhost", 55), self.servidor.obtener_direccion())
        self.servidor.obtener_socket().close()

    def test_AsignarDireccion(self):
        self.servidor = Servidor.Servidor("xxxx.xxxx.xxxx.xxxx", 0)
        self.servidor.asignar_direccion("localhost", 65)
        self.assertEqual(("localhost", 65), self.servidor.obtener_direccion())
        self.servidor.obtener_socket().close()

    def test_ObtenerSocket(self):
        self.servidor = Servidor.Servidor("xxxx.xxxx.xxxx.xxxx", 0)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.asignar_socket(self.mi_socket)
        self.assertEqual(self.mi_socket, self.servidor.obtener_socket())
        self.servidor.obtener_socket().close()

    def test_AsignarSocket(self):
        self.servidor = Servidor.Servidor("xxxx.xxxx.xxxx.xxxx", 0)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.asignar_socket(self.mi_socket)
        self.assertAlmostEqual(self.mi_socket, self.servidor.obtener_socket())
        self.servidor.obtener_socket().close()
    
    def test_ObtenerNumConexiones(self):
        self.servidor = Servidor.Servidor("xxxx.xxxx.xxxx.xxxx", 0)
        self.assertIsInstance(self.servidor.obtener_num_conexiones(), int)
        self.servidor.obtener_socket().close()

    def test_ObtenerConexiones(self):
        self.servidor = Servidor.Servidor("xxxx.xxxx.xxxx.xxxx", 0)
        total = 0
        self.assertEqual(total,self.servidor.obtener_num_conexiones())
        for i in self.servidor.obtener_conexiones():
            self.servidor.obtener_conexiones().append(random.randrange(total))
        self.assertEqual(total, self.servidor.obtener_num_conexiones())
        
    
    def test_ManejarConexiones(self):
        pass

    def test_EstablecerConexion(self):
        pass

    def test_AceptarConexiones(self):
        pass

    def test_Manejo(self):
        pass

    def test_EjecutarServidor(self):
        pass

    def test_INIT(self):
        self.servidor = Servidor.Servidor("xxxx.xxxx.xxxx.xxxx", 0)
        self.assertTrue(self.servidor)
        self.servidor.obtener_socket().close()

class TestCliente(unittest.TestCase):
      
    def test_ObtenerDireccion(self):
        self.cliente = Cliente.Cliente("xxxx.xxxx.xxxx.xxxx", 0)
        self.cliente.asignar_direccion("localhost", 55)
        self.assertEqual(("localhost", 55), self.cliente.obtener_direccion())
        self.cliente.obtener_socket().close()

    def test_AsignarDireccion(self):
        self.cliente = Cliente.Cliente("xxxx.xxxx.xxxx.xxxx", 0)
        self.cliente.asignar_direccion("localhost", 55)
        self.assertEqual(("localhost", 55), self.cliente.obtener_direccion())
        self.cliente.obtener_socket().close()

    def test_ObtenerSocket(self):
        self.cliente = Cliente.Cliente("xxxx.xxxx.xxxx.xxxx", 0)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.asignar_socket(self.mi_socket)
        self.assertEqual(self.mi_socket, self.cliente.obtener_socket())
        self.cliente.obtener_socket().close()

    def test_AsignarSocket(self):
        self.cliente = Cliente.Cliente("xxxx.xxxx.xxxx.xxxx", 0)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.asignar_socket(self.mi_socket)
        self.assertEqual(self.mi_socket, self.cliente.obtener_socket())
        self.cliente.obtener_socket().close()

    def test_ManejarMensajes(self):
        pass

    def test_EnviarMensajes(self):
        pass

    def test_RecibirMensajes(self):
        pass

    def test_EnviarMensaje(self):
        pass

    def test_EjecutarCliente(self):
        pass

    def test_INIT(self):
        self.cliente = Cliente.Cliente("xxxx.xxxx.xxxx.xxxx", 0)
        self.assertTrue(self.cliente)
        self.cliente.obtener_socket().close()


unittest.main(argv = ['ignored', '-v'], exit = False)