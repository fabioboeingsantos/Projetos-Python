'''
A classe Aluno
- Crie a classe alunos com nome e nota
- Crie 2 alunos com valores diferentes
- imprima o nome e a nota de cada um

2 parte
- reaproveite a classe aluno, crie o metodo 'situacao()'
- se a nota for >=6, mostre aprovado
- Caso contrario, mostre reprovado
- teste com os 2 alunos diferentes

'''


class Alunos():
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota
        
    def situacao(self):
        if self.nota >= 6:
            return "Aprovado " 
                
        else:
            return 'Reprovado'
        
    def exibir(self):
        print(f'Nome: {self.nome}, Nota: {self.nota} - Situacao {self.situacao()}')


aluno01 = Alunos("Fabio", 5.0)
aluno02 = Alunos("Fabiana", 8.0)


print('='*42 )
aluno01.exibir()
print('='*42 )
aluno02.exibir()
print('='*42 )

