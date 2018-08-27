import unittest
import Cliente

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente.Cliente()

    def TestInit(self):
        cliente = Cliente.Cliente()
        self.assertTrue(cliente)
    
    def TestEnviarMensaje(self):
        self.assertEqual(Cliente.enviarMensaje(), "")


if __name__ == '__main__':
    unittest.main()