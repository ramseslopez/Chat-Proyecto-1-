import unittest
import Cliente
import socket

class TestCliente(unittest.TestCase):

    
    def TestEnviarMensaje(self):
        self.c = Cliente.Cliente("localhost",5000)
        self.assertIsInstance(self.c.enviar_mensaje(), str)


if __name__ == '__main__':
    unittest.main()