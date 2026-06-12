

def situacao(self):
    soma_notas = sum(self.notas)
    media = soma_notas / len(self.notas)  
    
    if media >= 7:
            print("Aprovado ") 
                
    else:
            print('Reprovado')
