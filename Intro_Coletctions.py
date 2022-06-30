from os import remove


idade = [31, 39, 40, 18]
for i in idade:
    print(i)
print('#####################')     
idade.append(15)
for i in idade:
    print(i)
print('#####################')     
idade.remove(40)
idade.sort()
print(idade)

if(15 in idade):
    idade.remove(15)
    
print('#####################')    
idade.insert(0, 10)
print(idade)    

idades_no_ano_que_vem = []
for i in idade:
    idades_no_ano_que_vem.append(i + 1)

print(idades_no_ano_que_vem)

#ou

idades_no_ano_que_vem0 = [(i + 1) for i in idade]
print(idades_no_ano_que_vem0)

print('#####################')  

#Filtrando 

idades = [21, 24, 58, 31, 18]

for j in idades:  #Mostra a lista toda um por um 
    if(j > 21):
        print(j)
        
#ou 

idades_ = [(j) for j in idades if j > 21] #Mostra a lista toda
print(idades_)
    