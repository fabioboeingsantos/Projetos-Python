'''crie uma lista de produtos e outra lista de precos,
Use um for para exibir cada nome do produto e o preco dele

Agora adicione uma logica que se o prduto tem preco menos que 10 cove devera subir 10% o preco. 
Mude o print para que a sg desses produtos seja diferente, quando essa logica for aplicada, 
voce deve mostrar o nome, o preco origiinal e o preco atualizade tbm.

'''

produto = ['uva','banana','goiaba']
precos_atual = [10.5,40.7,75.3]

for posicao, produto in enumerate(precos_atual):
    #print(f'{produto} - R$ {precos[posicao]:}')
    
    if precos_atual[posicao] < 10:
        reajuste_preco = precos_atual * 0.1
        novo_preco = precos_atual + reajuste_preco       

print(f'Você vai ter um acréscimo de 10% {precos_atual}. Passou a custar R$ {novo_preco}:')



'''
#print(frutas[0],precos[0])
print(len(frutas))
desconto_porcento = 0.1
total
print(total_produtos)

'''