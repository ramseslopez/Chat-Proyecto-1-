import unittest
import Cliente

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente.Cliente()

    def TestInit(self):
        cliente = Cliente.Cliente()
        self.assertTrue(cliente)
    
    def TestEnviarMensaje(self):
        self.assertIsInstance(Cliente.enviarMensaje(), str)


if __name__ == '__main__':
    unittest.main()