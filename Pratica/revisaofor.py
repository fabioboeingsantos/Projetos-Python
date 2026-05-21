#1. Contagem simples - Mostre na tela os números de 1 até 10 usando for
for i in range(1,12,1):
    print(i)

#2. Contagem regressiva - Mostre os números de 10 até 1
for i in range(1,-12,-1):
    print(i)

#3. Soma de números - Peça um número ao usuário e some todos os números de 1 até ele.
numero = int(input('digite um numero; '))
soma_total = 0  
for i in range(1, numero + 1):
    soma_total += i
    print(f' resultado {soma_total}')
    

#4. Tabuada
numero = int(input('Digite um numero; '))
print(f'\ntabuada do {numero}')
for i in range(1,11):
    resultado = numero * 1
    print(f'{numero} x {i} = {resultado}')

  
#5. Contador de pares - Mostre todos os números pares de 1 até 20.
print('Numeros pare de 1 a 20: ')
for numeros in range(1,21):
    if numeros % 2 == 0:
        print(numeros)
       

#6. Contador de ímpares - Mostre os números ímpares de 1 até um número digitado pelo usuário.
limite = int(input('Digite um numero: '))
print(f'Numeros impares de 1 ate {limite}')

for numero in range(1, limite +1):
    if numero % 2 != 0:
        print(numero)


#7. Soma apenas dos pares - Some apenas os números pares de 1 até um número digitado.
limite = int(input('Digite um numero: '))
soma_pares = 0
for i in range(1, limite + 1):
    if i % 2 == 0:
        soma_pares += i
        print(f'A s soma dos numeros pares de 1 ate o {limite} e {soma_pares}')


#8. Média de valores - Peça ao usuário 5 números e calcule a média deles.
soma_total = 0
for i in range(1,6):
    numero = float(input(f'Digite o {i} numero: '))
soma_total += numero
media = soma_total / 5
print (f'\nSoma total: {soma_total}')
print (f'Media final: {media}')


#9. Contar positivos e negativos - Peça 5 números e diga quantos são positivos e quantos são negativos.
positivo = 0
negativo = 0
print("Digite 5 numeros (podem ser negativos ou positivos): \n")

for i in range(1,6):
    numero = float(input(f'Digite o {i} numero:' ))
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
        
print('\n--- Resultado Final ---')
print(f'Quantidade de positivos: {positivo}')
print(f'Quantidade de negativos {negativo}')


#10. Maior número - Peça 5 números e mostre qual é o maior
print('Digite 5 numero e eu direi qual e o maior: ')
maior_numero = float(input('Digite o 1 numero: '))
for i in range(2,6):
    numero = float(input('Digite o {i} numero: '))
    if numero > maior_numero:
        maior_numero = numero
print(f'O maior numero digitado foi {maior_numero}')