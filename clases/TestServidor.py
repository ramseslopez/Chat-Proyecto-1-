import unittest
import Servidor

class TestServidor(unittest.TestCase):

    def setUp(self):
        self.servidor = Servidor.Servidor()

    def TestInit(self):
        servidor = Servidor.Servidor() 
        self.assertTrue(servidor)
        
    def TestManejo(self):
        self.assertIsNotNone(Servidor.manejo())

    def TestEjecutar(self):
        self.assertTrue(Servidor.ejecutar())


if __name__ == '__main__':
    unittest.main()
