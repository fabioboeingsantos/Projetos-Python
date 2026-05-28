'''Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre a sua media'''

print("=" *30 )
print(f'{"MÉDIA DO ALUNO":^30}')
print("=" *30 )

nota01 = float(input('Digite sua primeira nota: '))
nota02 = float(input('Digite sua segunda nota: '))

media = (nota01 + nota02) / 2
print('A media entre {:} e {} e igual a {}'.format(nota01, nota02, media))

