from operator import attrgetter
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
        
    def __eq__(self, outro): #Equal ou igual 
        if type(outro) != ContaSalario and not isinstance(outro, ContaSalario): #Checando tipo do Objeto 
            return False 
        
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
    def __lt__(self, outro):  #Less Than ou Menor que 
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        
        return self._codigo < outro._codigo
        
    def deposita(self, valor):
        self._saldo += valor  
        
    def __str__(self) -> str:
        return f'[>>Codigo: {self._codigo}  Saldo: {self._saldo}]'  
    
class ContaMultiplaSalaraio(ContaSalario):
    pass     
    
    
conta1 = ContaSalario(123)
conta1.deposita(1000)
print(conta1)  

conta2 = ContaMultiplaSalaraio(123)
conta2.deposita(1000)
print(conta2)

conta3 = ContaSalario(12) 
conta3.deposita(1000)     

print(conta1 == conta2)

contas = [conta1, conta2, conta3]

print(conta1 >= conta2)

for conta in sorted(contas):
    print(conta)

# for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):   #Jeito de acessar um atributo privado um pouco mais de boa 
#     print(conta)