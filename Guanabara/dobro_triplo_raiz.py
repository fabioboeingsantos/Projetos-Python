''' Crie um algoritmo que leia um numero e mostre o seu dobro, tripl e raiz quadrada.'''

numero = int(input("Digite um numero: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print('O dobro de {} vale {}.'.format(numero, dobro))
print('O triplo de {}, vale {}, \na raiz quadrada  de {}, vale {:.2f}.'.format(numero, triplo, numero , raiz_quadrada))

#nao esquendo a contra barra n pula a linha.
#{:.2f} formatacao do numero, casas decimais.

#Uma forma, resumida sem as variaveis

numero = int(input("Digite um numero: "))
print('O dobro de {} vale {}.'.format(numero, (numero*2)))
print('O triplo de {}, vale {}, \na raiz quadrada  de {}, vale {:.2f}.'.format(numero, (numero*3), numero, numero**(1/2)))
#nao esquecer de colocar os () no numero*2 para ele calcular o numero especifico.