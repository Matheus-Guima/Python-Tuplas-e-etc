class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo 
        self.saldo = 0 
        self.contas = []
        
    def deposita(self, valor): 
        self.saldo += valor 
        return self.saldo
        
    def __str__(self) -> str:
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"
    

                
conta_do_gui = ContaCorrente(15) 
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)   

conta_da_dani = ContaCorrente(47685)
print(conta_da_dani)


contas = [conta_do_gui, conta_da_dani] #Listas são mutáveis (Pode adcionar, remover elementos)
for conta in contas:
    print(conta)
    
#Tupla - É  imutável 
guilherme = ('Guilherme', 37, 1981) #Não tem append 
daniela = ('Daniela', 31, 1987)

#Explo de como mexer na tupla 
def deposita(conta): #Variação "funcional" (separando o comportamento dos dados)
    codigo = conta[0]
    novo_saldo = conta[1] + 100
    return (codigo, novo_saldo) 

conta_da_dani = deposita(conta_do_gui)

#Lista de Tuplas 
usaurios = [guilherme, daniela]
print(usaurios)

usaurios.append(('Paulo', 39, 1987))
print(usaurios)

###################

conta_do_gui = ContaCorrente(15) 
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)   

conta_da_dani = ContaCorrente(47685)
print(conta_da_dani)

contas_ = (conta_do_gui, conta_da_dani) #Tupla 

contas_[0].deposita(300) # É mutável, ta apontando pro objeto da lista dentro da tupla 
#TUPLAS NORMALMENTE SÃO USADOS QUANDO DEVE-SE MANTER UM PADRÃO OU ORDEM DENTRO 



    
    
    