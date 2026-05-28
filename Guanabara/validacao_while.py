'''Faca um programa que leia o sexo de uma pesso, mas so aceite os valor "m" ou f, caso esteja errado,
peca a digitacao novamente ate ter um valor correto. '''

sexo = input("Informe seu sexo: [M ou F] ")
 #condicao
while sexo not in ["M", 'F']:
    sexo = str(input("Dados invalidos, Informe seu sexo [M ou F].")).upper().strip()
print(f'O sexo, {sexo} foi registrado com sucesso')