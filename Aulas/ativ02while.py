'''O usuario digita os numeros ate digitar o 0,
conte quantos numeros foram digitados(sem contar o 0)'''

contador = 0

numero = int(input('Digite um numero: ' ))

while numero != 0:
    contador += 1

    numero = int(input('Digite o proximo numero: '))

print(f" voce digitou {contador} numeros. ")