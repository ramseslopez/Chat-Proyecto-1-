# Chat (Proyecto 1)

* **López Soto Ramses Antonio**
* **Facultad de Ciencias UNAM**
* **Modelado y programación**

_Se llevará a cabo el desarrollo de un sofware que simule un chat sencillo_

## Comenzando 🚀

_Para el desarrollo del siguiente software se utilizaron sockets e hilos de ejecución principalmente_

### Pre-requisitos 📋

* Python 3.5.2 
* Tkinter 8.6

### Instalación 🔧

_Si no se tiene instalado python 3, ejecute el siguiente comando en Terminal:_

### Ubuntu

```
sudo apt-get install python3.5
```

### Fedora

```
sudo dnf install python3.5
```

_Para verificar que la instalación de python fue exitosa, ejecuta el siguiente comando en Terminal:_

```
$ python3 --version
python 3.5.6
```

_Para instalar Tkinter, ejecute el siguiente comando:_

### Ubuntu

```
sudo apt-get install python3-tk
```

### Fedora

```
sudo dnf install python3-tkinter
```

_Para verificar que la instalacion de Tkinter fue existosa, haga lo siguiente:_

```
$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter
>>> tkinter.TkVersion
8.6
>>> tkinter._test()
```

## Pruebas unitarias ⚙️

_Para las pruebas unitarias se utilizo el módulo unittest._

_Para ejecutar las pruebas ejecutar las pruebas, ejecutar el siguiente comando:_

```
./test.sh
```

## Documentación 🖇️

_Para obtener la documentación, ejecutar el siguiente comando:_

```
./doc.sh
```

## Ejecución
__Para ejecutar el servidor utilice el siguiente comando:__

```
python3 proyecto/pruebas/chat/clases/Servidor.py
```

__Para ejecutar el cliente utilice el siguiente comando pasando como argumanto una dirección IP:__

```
python3 proyecto/pruebas/chat/clases/Cliente.py 127.0.0.1
```

## Construido con 🛠️

* Python 3.5.2
* Tkinter 8.6

## Autor ✒️
* **Ramses Antonio López Soto** - [ramseslopez](https://github.com/ramseslopez)

---
⌨️ con ❤️ por [ramseslopez](https://github.com/ramseslopez) 😊