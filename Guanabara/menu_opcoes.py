'''Crie um programa que leia dois valores e mostre um MENU 
Seu programa devera realizar a operacao solicidada em cada caso.

1 - soma
2 - multiplicador
3 - maior
4 - novos numero
5 - sair

'''
from time import sleep
numero01 = int(input('Digite o primeiro valor: '))
numero02 = int(input('Digite o segundo valor: '))
Opcao = 0


menu = '''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numero
[5] Sair
'''
print(menu)

Opcao = int(input('Digite sua opcao: '))
while Opcao != 5:
    print(menu)
    Opcao = int(input('Digite sua opcao novamente: '))
    if Opcao == '1':
        total = numero01 + numero02
        print(f'A soma entre {numero01} + {numero02} = {total}.')
    elif Opcao == '2':
        total = numero01 * numero02
        print(f'O resultado entre {numero01} x {numero02} = {total}.')
    elif Opcao == "3":
        if numero01 > numero02:
            maior = numero01
        else: maior = numero02
        print(f' O maior entre {numero01} e {numero02} e {maior}')
    elif Opcao == '4':
        print('Informe os numero novamente: ')
        numero01 = int(input('Digite o primeiro valor: '))
        numero02 = int(input('Digite o segundo valor: '))
    elif Opcao == '5':
        print('Finalizando')
    sleep(2)

print('Saindo')
