import array as arr 
import numpy as np

#Para ter uma eficácia maior quando estiver trabalhando com numeros Existem tipos específicos 
arr.array('d', [1, 3.5])  #Falar tipo e todos elementos tem que ser do mesmo tipo 

#Tenta armazenadr valor de maneira eficiente 
#No dia a dia do Python, mais comum usar as listas 
#Para situações bem específicas usar Listas 

#Onde costuma ser importante alto desenpenha de fuções matemáticas com pyhton, tem uma biblioteca chamada numpy: import numpy as np; pip install numpy

numeros = np.array([1, 3.5])
print(numeros)