'''Peca ao usuario uma idade entre 0 e 120, enquanto for invalida, continue pedindo'''

idade = 10
numero = 0
'''
while numero != idade:
    numero = int(input('Digite sua idade '))
    if numero > 120:
        print('Acima')
        '''
        

idade = -1

while idade < 0 or idade > 120:
    idade = int(input("Digite uma idade válida (0 a 120): "))

    if idade < 0 or idade > 120:
        print("Idade inválida! Tente novamente.")

print(f"Obrigado! A idade digitada foi {idade}")