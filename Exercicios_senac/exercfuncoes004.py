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

def depositar (saldo):
    valor = float(input('Digite quanto deseja depositar:'))
    saldo = valor + saldo
    print(f'Voce depositou {valor:.2f}, Seu saldo atual\n R$:{saldo:.2f}')
    return saldo

def sacar(saldo):
    valor = float(input('Digite quanto voce deseja sacar: '))
    
    if valor > saldo:
        print('Saldo insuficiente')
    else:
        saldo = saldo - valor
        print (f'Voce sacou R$: {valor:.2f}, Saldo restante {saldo:.2f}')
    return saldo
   

def Saldo_total(saldo):
    print(f'Seu saldo total e de R$:{saldo}')
    return saldo

    

while True:
    menu_simples()
    opcao = int(input('Escolha sua opcao: '))

    if opcao == 0:
        print('Sair')
        break

    elif opcao == 1:
        saldo = depositar(saldo)
        
    elif opcao == 2:
        saldo = sacar(saldo)

    elif opcao == 3:
        Saldo_total(saldo)

    else:
        print('encerrando')