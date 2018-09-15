import unittest
import Cliente
import socket

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