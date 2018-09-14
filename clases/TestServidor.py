import unittest
import Servidor
import socket

class TestServidor(unittest.TestCase):

    def test_ObtenerDireccion(self):
        self.servidor = Servidor.Servidor("localhost", 55)
        self.servidor.asignar_direccion("localhost", 55)
        self.assertEqual(("localhost", 55), self.servidor.obtener_direccion())
        self.servidor.obtener_socket().close()

    def test_AsignarDireccion(self):
        self.servidor = Servidor.Servidor("localhost", 55)
        self.servidor.asignar_direccion("localhost", 55)
        self.assertEqual(("localhost", 55), self.servidor.obtener_direccion())
        self.servidor.obtener_socket().close()

    def test_ObtenerSocket(self):
        self.servidor = Servidor.Servidor("localhost", 55)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.cerrar_socket()
        self.servidor.asignar_socket(self.mi_socket)
        self.assertAlmostEqual(self.mi_socket, self.servidor.obtener_socket())
        self.servidor.obtener_socket().close()

    def test_AsignarSocket(self):
        self.servidor = Servidor.Servidor("localhost", 55)
        self.mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.cerrar_socket()
        self.servidor.asignar_socket(self.mi_socket)
        self.assertAlmostEqual(self.mi_socket, self.servidor.obtener_socket())
        self.servidor.obtener_socket().close()
    
    def test_ObtenerConexiones(self):
        self.servidor = Servidor.Servidor("localhost", 55)
        self.assertIsInstance(self.servidor.obtener_conexiones(), int)
        self.servidor.obtener_socket().close()
    
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

    def test_CerrarSocket(self):
        self.servidor = Servidor.Servidor("localhost", 55)
        self.assertIsNone(self.servidor.cerrar_socket())

    def test_INIT(self):
        self.servidor = Servidor.Servidor("localhost", 55)
        self.assertTrue(self.servidor)
        self.servidor.obtener_socket().close()
        
unittest.main(argv=['ignored', '-v'], exit=False)
