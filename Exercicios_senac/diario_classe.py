class Alunos():
    def __init__(self, nome: str, notas: []):
        self.nome = nome
        self.notas = notas
        
    def exibir(self):        
        print(f'Nome: {self.nome}, media: {self.media} ')

    #def de somar, logica de somar, por dizer se esta aprovado ou reprovado    
    def situacao(self):
        sum(self.notas)
        media = self.somar() / len(self.notas)  
        if media >= 7:
            print("Aprovado") 
                
        else:
            print('Reprovado')

def menu_simples():
    print('='*30)
    print(f'\n{"Cadastro de alunos":^30}')
    print('\n(1) - Cadastrar Aluno')   
    print('(2) - Lancar notas')
    print('(3) - Ver Situacao')
    print('(4) - listar alunos')
    print('(0) - Sair')
    print('\n' +'='*30)

def cadastrar_alunos():
    print('\nCadastrando ALuno')
    nome = input('Digite seu nome: ')
    novo_aluno = Alunos(nome)
    lista_de_alunos.append(novo_aluno)
    print(f'{nome} cadastrado com sucesso. ')

def cadastrar_notas():
    print('\nCadastrando Notas')
    indice = float(input('Digite sua nota: '))
    
    


def listar_alunos():
    print(f'\n{'Listando Aluno':^30}')
    if not lista_de_alunos:
        print('Nao esta na lista. ')
        
    else:
        for aluno in lista_de_alunos:
           aluno.exibir()
    print('='*30)
    
def situacao(self):
        sum(self.notas)
        media = self.somar() / len(self.notas)  
        if media >= 7:
            print("Aprovado ") 
                
        else:
            print('Reprovado')

lista_de_alunos = []


while True:
    menu_simples()
    Opcao = input('Digite sua opcao: ')

    if Opcao == '0':
        break

    elif Opcao == '1':
        cadastrar_alunos()
    
    elif Opcao == '2':
        cadastrar_notas()

    elif Opcao == '3':
        situacao()  


    elif Opcao == '4':
        listar_alunos()

    else:
        print('Opcao invalida')