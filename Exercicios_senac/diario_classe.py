
class Alunos():
    def __init__(self, nome: str, notas: []):
        self.nome = nome
        self.notas = notas
        
    def exibir(self):        
        print(f'Nome: {self.nome}, notas: {self.notas} ')

   
    def situacao(self):
        if not self.notas:
            print(f'O aluno {self.nome}, ainda nao possui notas cadastradas. ')
            return                                          #usado para interromper, faz a checagem e voltar ao menu... nao esquecer desse ***...

        soma_das_notas = sum(self.notas)
        media = soma_das_notas / len(self.notas)  


        if media >= 7:
            print(f'A media foi de {media:.2f} - Voce esta Aprovado') 
                
        else:
            print(f'A media foi de {media:.2f} - Voce esta Reprovado')



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
    novo_aluno = Alunos(nome,[])                            # adicinar uma lista vazia aqui, em referencia a classe, nome, notas []
    lista_de_alunos.append(novo_aluno)
    print(f'{nome} cadastrado com sucesso. ')

def lancar_notas():
    print('='*30)
    print('\nCadastrando Notas')

    if not lista_de_alunos:
        print('Nenhum aluno cadastrado')
        return                                  #usado para interromper e voltar ao menu


    for posicao, aluno in enumerate(lista_de_alunos):           #busca na lista a posicao do aluno
        print(f'{posicao + 1} - {aluno.nome}')

    num_aluno_escolhido = int(input('Adicione o aluno de acordo com numero da lista: '))    #input com a selecao do enumerate

    indice = num_aluno_escolhido -1
    aluno = lista_de_alunos[indice]

    nota_adicionada = float(input('Adicione sua nota: '))    
    aluno.notas.append(nota_adicionada)    

    print(f'{aluno.nome} - {nota_adicionada:.2f} adicionada com sucesso. ')
    


def ver_situacao():
    if not lista_de_alunos:
        print('Nenhum aluno cadastrado: ')
        return                                              #usado para interromper, faz a checagem e voltar ao menu...

    for posicao, aluno in enumerate(lista_de_alunos):
        print(f'{posicao + 1} - {aluno.nome}')

    num_aluno_escolhido = int(input('Digite o aluno de acordo com o numero da lista: '))

    indice = num_aluno_escolhido -1
    aluno = lista_de_alunos[indice]                         #Nao posso esquecer desse detalhe de definir o indice de inicio do codigo

    aluno.situacao()


def listar_alunos():
    if not lista_de_alunos:
        print('Nenhum aluno cadastrado.')
        return


    for posicao, aluno in enumerate(lista_de_alunos):
       print(f' {posicao + 1} {aluno}')
       aluno.exibir()

lista_de_alunos = []


while True:
    menu_simples()
    Opcao = input('Digite sua opcao: ')

    if Opcao == '0':
        break

    elif Opcao == '1':
        cadastrar_alunos()
    
    elif Opcao == '2':
        lancar_notas()

    elif Opcao == '3':
        ver_situacao()  

    elif Opcao == '4':
        listar_alunos()

    else:
        print('Opcao invalida')