#Saber todas as posições dos números 


idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])
    
    


#list(range(len(idades)))   #Forçando a geração dos valores

print('####################################')

#ENUMERATE

#enumerate(idades) - imprime local armazenado do obj

list(enumerate(idades)) #Vai imprimir tuplas

for valor in enumerate(idades):
    print(valor)
    
#DESEMPACOTANDO

for indice, idade in enumerate(idades):
    print(indice, idade)

print('####################################')
    
#Mais exemplos de desempacotamento 

usuarios = [
    ("Matheus", 25, 1997),
    ("Ana", 25, 1997),
    ("Beatriz", 19, 2003)
]    

for nome, idade, ano in usuarios: 
    print(nome) #Usando só o nome 
    
#ou    

# for nome, _, _ in usuarios:  #O underscore siginifica ppara ignorar as outras possibilidades de print dentro da tupla
#     print(nome) 