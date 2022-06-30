#Geradores comuns de iteráveis 

#not in place

idades = [15, 87, 32, 65, 56, 32, 49, 37]
print(idades, 'Desordenado')


print(sorted(idades)) #Ordena menor para o maior 

print(list(reversed(idades))) #Inverte a ordem

print(sorted(idades, reverse=True)) #Ordena maior para o menor 

print(list(reversed(sorted(idades)))) #Ordena do maior para o menor e inverte a ordem


#in pla 
idades.sort() #in place
print(idades, 'in place')
