import Servidor
import Cliente
import sys

s = Servidor.Servidor()

if (len(sys.argv) > 1):
    c = Cliente.Cliente(sys.argv[1])
else:
    s.ejecutar()