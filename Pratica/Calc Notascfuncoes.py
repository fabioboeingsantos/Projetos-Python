#Calculo de Notas com Funções

notas = int(input('Digite a quantidade de notas que deseja adicionar: '))
notas_lista = []
for i in range(notas):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas_lista.append(nota)    

media = sum(notas_lista) / len(notas_lista)
print(f'A média das notas é: {media:.2f}')

if media < 5:
    print('Voce esta Reprovado')  
elif media >= 5 and media < 7:
    print('voce esta em Recuperação')
else:    print('Voce esta Aprovado')

