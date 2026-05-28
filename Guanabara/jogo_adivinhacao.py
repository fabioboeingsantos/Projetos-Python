'Faca um jogo onde o jogador precisa adivinhar um numero entre 0 e 10, e vai ficar tentando ate conseguir.'

from random import randint 
computador =  randint(0,10)
print('Adivinhe um numero entre 0 e 10')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Qual e o seu palpite? "))
    palpites += 1                        # palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... tenta novamente")
        elif jogador > computador:
            print('Menos, tente novamente...')
            
print(f'Acertou com tantos {palpites} palpites')