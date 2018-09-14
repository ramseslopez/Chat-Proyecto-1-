import unittest
import Cliente
import socket

class TestCliente(unittest.TestCase):

    
    def test_ObtenerDireccion(self):
        self.cliente = Cliente.Cliente("localhost", 55)
        self.cliente.asignar_direccion("localhost", 55)
        self.assertEqual(("localhost", 55), self.cliente.obtener_direccion())
        self.cliente.obtener_socket().close()

    def test_AsignarDireccion(self):
        self.cliente = Cliente.Cliente("localhost", 55)
        self.cliente.asignar_direccion("localhost", 55)
        self.assertEqual(("localhost", 55), self.cliente.obtener_direccion())
        self.cliente.obtener_socket().close()
        pass

    def test_ObtenerSocket(self):
        self.cliente = Cliente.Cliente("localhost", 55)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.cerrar_socket()
        self.cliente.asignar_socket(self.mi_socket)
        self.assertEqual(self.mi_socket, self.cliente.obtener_socket())
        self.cliente.obtener_socket().close()

    def test_AsignarSocket(self):
        self.cliente = Cliente.Cliente("localhost", 55)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.cerrar_socket()
        self.cliente.asignar_socket(self.mi_socket)
        self.assertEqual(self.mi_socket, self.cliente.obtener_socket())
        self.cliente.obtener_socket().close()

    def test_ManejarMensajes(self):
        #self.cliente = Cliente.Cliente("localhost", 55)
        pass

    def test_EnviarMensajes(self):
        #self.cliente = Cliente.Cliente("localhost", 55)
        pass

    def test_RecibirMensajes(self):
        #self.cliente = Cliente.Cliente("localhost", 55)
        pass

    def test_EnviarMensaje(self):
        #self.cliente = Cliente.Cliente("localhost", 55)
        pass

    def test_EjecutarCliente(self):
        #self.cliente = Cliente.Cliente("localhost", 55)
        pass

    def test_INIT(self):
        self.cliente = Cliente.Cliente("localhost", 45)
        self.assertTrue(self.cliente)
        self.cliente.obtener_socket().close()


unittest.main(argv=['ignored', '-v'], exit=False)