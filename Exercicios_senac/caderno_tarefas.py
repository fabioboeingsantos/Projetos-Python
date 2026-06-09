'''
Caderno de tarefas - Exercícios de Funções

As tarefas ficam em uma lista, cada opcao chama uma funcao que recebe
essa lista como paramentro para adicionar, listar ou remover itens.

1.Calcular
2 Listar
3 Remover
0 Sair

crie a lista vazia tarefas = [] antes do while
passe a lista como parametro: adicionar_tarefa(lista)
use lista.append() para adicionar itens, para adicionar e lista.pop(i) para remover.
numere com enumerate(lista, start=1) dentro do for.
o usuario ve de 1 em diante, mas a lista comeca em 0, entao subtraia 1.

'''
Tarefa = []

def menu_simples ():
    print('='*30 )
    print(f'\n{"Menu de Frases":^30}')
    print('\n 1 - Adicionar')
    print(' 2 - Listar')
    print(' 3 - Remover')
    print(' 0 - SAIR\n')
    print('='*30 )


def adicionar_tarefa(lista):
    tarefa = input('Digite a tarefa: ')
    
    lista.append(tarefa)    
    print(f'A Tarefa "{tarefa}" foi adicionada com sucesso, a lista atualizada contem {len(lista)} tarefa(s).')
    
def listar_tarefas(lista):
    if not lista:
        print('Nenhuma tarefa cadastrada.')
    else:
        print('Tarefas:')
        for posicao, tarefa in enumerate(lista , start=1):
            print(f'{posicao } - {tarefa}')

def remover_tarefa(lista):
    numero_remover = int(input('Digite o número da tarefa que deseja remover: '))
    indice = numero_remover - 1
    if indice < 0 or indice >= len(lista):
        print('Numero invalido.')
    
    elif lista:
        for posicao, tarefa in enumerate(lista):
            if posicao == numero_remover: lista.pop(posicao)
            print(f'A tarefa "{tarefa + 1}" foi removida com sucesso.')
                    

while True:
    menu_simples()
    opcao = input('Escolha uma opção: ')

    if opcao == '0':
        print('Saindo.')
        break

    elif opcao == '1':
        adicionar_tarefa(Tarefa)
                    
    elif opcao == '2':
        listar_tarefas(Tarefa)
    
    elif opcao == '3':
        remover_tarefa(Tarefa)
    else:
        print('Opção inválida')


