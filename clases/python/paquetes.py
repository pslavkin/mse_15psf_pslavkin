|-- paquete
|   |-- __init__.py
|   |-- mi_modulo1
|   |   |-- mod1_file1.py
|   |-- mi_modulo2
|   |   |-- __init__.py
----------------------------

lo invoco como:
---------------------------
from paquete.mi_modulo1 import mod1_file1 as m1
m1.mod1_file1_func1()

