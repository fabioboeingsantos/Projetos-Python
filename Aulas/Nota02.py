#Aprovado - reprovado

primeiro_semestre = float(input('Digite sua nota do primeiro semestre '))
segundo_semestre = float(input('digite sua nota do segundo semestre '))
terceiro_semestre = float(input('digite sua do terceiro semestre '))

media = (primeiro_semestre + segundo_semestre + terceiro_semestre) / 3
print(media)

if media < 5:
    print('Nao atendido, voce esta em recuperacao')

elif media >= 6 and media <= 7:
    print("Regular")

elif media >= 8:
    print('Atendido')




