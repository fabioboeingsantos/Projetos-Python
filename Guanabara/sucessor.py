#Opcao usando 3 variaveis
'''
numero = int(input('Digite um valor: '))
antecessor = numero - 1
sucessor = numero + 1
print(' o valor analisado foi {}, seu antecessor e {}, e antecessor e {} '.format(numero, antecessor, sucessor))
'''
#Opcao com uma variavel

numero = int(input('Digite um valor: '))
print('Valor analisado {}, o seu antecessor e {}, e o sucessor e {}.'.format(numero, (numero-1), (numero + 1)))