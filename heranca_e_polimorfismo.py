from abc import abstractmethod
from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
         
    def deposita(self, valor):
        self._saldo += valor
    
    @abstractmethod #Torna obrigatório todas as classe filhas implementarem esse método   
    def passa_o_mes(self):
        pass    
        
    
    def __str__(self) -> str:
        return f"[>>Código: {self._codigo} Saldo: {self._saldo}]"
    

class ContaCorrente(Conta): #Herança
    def passa_o_mes(self):
        self._saldo -= 2
        
class ContaPoupanca(Conta): #Herança        
    def passa_o_mes(self):
        por_cento = self._saldo * 0.01
        self._saldo += por_cento
        self._saldo -= 3 
        
class ContaInvestimento(Conta): #Vai dar erro, não implementou método passa_o_mes
    pass        
        
print('####################')
       
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16) 

print('---------------')

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

print('---------------')

conta18 = ContaInvestimento(18)
conta18.deposita(1000)
conta18.passa_o_mes()
print(conta18)     
 
print('####################')

contas = [conta16, conta17]  
for conta in contas:
    conta.passa_o_mes() #duck typing
    print(conta)            