'''nota = 8    
falta = 12

nota = int(input('Digite sua nota. '))

if nota >= 7 or falta <= 16:
    print('Aprovado')
else:
    print('Reprovado.')
    '''
'''
#Peca ao usuaria um numero e diga se ele e positivo, negativo ou igual a zero.
Numero = int(input("Digite um numero: "))

if Numero > 0:
    print('positivo')
elif Numero < 0:
    print('negativo')
else:
    print('0')
    '''

'''Peca o nome do usuario e senha, cada um com sua variavel. Considere o usuario correto como "admin"
e a senha como "1234",
- Se ambos estiverem corretos, exiba "acesso permitido"
- Caso contrario, exiba "o usuario ou senha invalidos"
'''

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

usuario_correto = 'admin'
senha_correta = '1234'


if usuario == usuario_correto and senha == senha_correta:
    print('Acesso permitido')
else:
    print("Usuário ou senha inválidos")