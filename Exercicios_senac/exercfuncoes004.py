'''
            Conta bancaria

Simule operacoes de uma conta, O saldo comeca em 0,
no programa principal, As funcoes que mudam o saldo devem retornar o saldo atualizado.

1 depositar - soma um valor ao saldo
2 sacar - subtrai, se houver saldo
3 ver saldo - exibe o saldo atual
0 sair - encerra o programa

- Guarde o retorno de volta, saldo = depositar(saldo, valor)
- ver_saldo(saldo) so imprime, nao precisa retornar.
- no saque, compare valor > saldo antes de subtrair.
- 

'''

def menu_simples ():
    print('='*30 )
    print(f'\n{"Conta Bancaria":^30}')
    print('\n 1 - Depositar')
    print(' 2 - Sacar')
    print(' 3 - Saldo')
    print(' 0 - SAIR\n')
    print('='*30 )

saldo = 0.0

def depositar(saldo, n2 ):
    

while True:
    menu_simples()
    opcao = int(input('Escolha sua opcao: '))

    if opcao == 0:
        print('Saindo')
        break

    
