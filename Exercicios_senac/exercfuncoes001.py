def menu_simples ():
    print('='*30 )
    print(f'{"Menu de Frases":^30}')
    print(' 1 - Saudação')
    print(' 2 - Sobre')
    print(' 3 - Ajuda')
    print(' 0 - SAIR')
    print('='*30 )

while True:
    menu_simples()
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        print('Bem-vindo ao nosso programa!')
    elif opcao == '2':
        print('Este programa nos vivemos entre altos e baixos.')
    elif opcao == '3':
        print('Para usar o programa, basta digitar o número da opção de acordo com o menu.')
    elif opcao == '0':
        print('Saindo do programa.')
        break
    else:
        print('Opção inválida, digite uma opção de acordo com o menu.')

'''
def saudacao():
    print('Bem-vindo ao nosso programa!')

def sobre():
    print('Este programa nos vivemos entre altos e baixos.')

def ajuda():
    print('Para usar o programa, basta digitar o número da opção de acordo com as opcoes.')

'''
