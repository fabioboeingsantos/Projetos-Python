'''
'Desafio: Auto Peças e Oficina'

'''
#variaveis
produtos = ['Pneu', 'Bateria', 'Óleo', 'Palheta']
servicos = ['Alinhamento', 'Revisão', 'Lavagem_completa', 'polimento']

preco_produtos = [430.99, 490.99, 149.99, 95.99]
preco_servicos = [55.99, 399.99, 40.99, 350,00]

#input
servico_produto_selecionado = input('"Você deseja ver nossos Produtos ou Servicos?"')

if servico_produto_selecionado == 'produtos':
    for posicao, produto in enumerate(produtos):
        print(f'{posicao +1 } - {produto} - R$: {preco_produtos[posicao]}.')

elif servico_produto_selecionado == 'servicos':
    for posicao, servico in enumerate(servicos):
            print(f'{posicao +1} - {servico} - R$: {preco_servicos[posicao]}.')
else:
    print('Opcao invalida. Digite "produtos" ou "Servicos?". ')
    exit()

numero_selecionado = int(input('Digite o número do item que deseja comprar: '))

indice = numero_selecionado -1

if numero_selecionado <= 0 or numero_selecionado > len(produtos) or numero_selecionado > len(servicos):
     print(f'Opcao invalida, Digite o numero de acordo com o produto, entre 1 e {len(produtos)}.')

elif servico_produto_selecionado == 'produtos':
    item_comprado = produtos[indice]
    preco = preco_produtos[indice]
    preco_cheio = preco
    
    if preco > 300:
        preco = preco * 0.9
        print(f'O produto selecionado foi {produtos[indice]}, e custa R$ {preco_produtos[indice]}, \nvoce tem direito a 10% de desconto, e passou a custar {preco}')
    else:
     print(f'O produto selecionado foi {produtos[indice]}, e custa R$ {preco_produtos[indice]}.')

elif servico_produto_selecionado == 'servicos':
    item_comprado = servico[indice]
    preco = preco_servicos[indice]
    preco_cheio = preco

    if preco > 300:
        preco = preco * 0.9
        print(f'O servico selecionado foi {servicos[indice]}, e custa R$ {preco_servicos[indice]},\nvoce tem direaito a 10% de desconto, e passou a custar {preco}.2f ')
    else:
     print(f' o servico selecionado foi {servicos[indice]}, e custa R$ {preco_servicos[indice]}.2f')

print('\n')
print('Auto Peças e Oficina')
print('Blumenau - SC')
print('27/05/2026')
print('         CUPOM FISCAL             ')
print('Item                         Valor')
print(f'{item_comprado}                   R$: {preco_cheio}')
if preco < preco_cheio:
    desconto = preco_cheio - preco
print(f'Desconto de 10%    R${desconto:.2f}')
print(f'TOTAL A PAGAR         R$ {preco:>10.2f}')