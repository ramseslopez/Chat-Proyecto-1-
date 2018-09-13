import unittest
import Servidor
import socket

class TestServidor(unittest.TestCase):

    def TestGetSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor()
        self.assertEqual(self.servidor,self.socket.getSocket())
        self.socket.close()

    def TestGetConexiones(self):
        #servidor = Servidor.Servidor()
        self.assertEquals(20, Servidor.getConexiones())
        
if __name__=='__main__':
    unittest.main()
