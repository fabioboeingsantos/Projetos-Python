#Nota Atendido Ou Nao atendido

nota = float(input("Digite a nota do aluno: "))

if nota < 5:
    print('nao atendido')

elif nota > 5.1 and nota <= 6.5:
    print('regular')

elif nota > 6.6 and nota <= 10:
    print('atendido')

else:
    print('numero nao condiz com uma nota de 0 a 10')
