'''
'Desafio: Auto Peças e Oficina'

'''
#variaveis
produtos = ['Pneu', 'Bateria', 'Óleo', 'Palheta']
servicos = ['Alinhamento', 'Revisão', 'Lavagem_completa', 'lavagem_ducha']

preco_produtos = [230.00, 490.00, 149.99, 95.5]
preco_servico = [55.00, 199.99, 40.00, 20.00]

#input
servico_produto_selecionado = input('"Você deseja ver nossos Produtos ou Servicos?"')

if servico_produto_selecionado == 'produtos':
    for posicao, produto in enumerate(produtos):
        print(f'{produto} {preco_produtos[posicao]:}')

elif servico_produto_selecionado == 'servicos':
    for posicao, servicos in enumerate(servicos):
            print(f'{servicos} {preco_servico[posicao]:}')
else:
    print('Digite para ver nossos produtos ou serviços?')

produto_selecionado = input('Digite o número do item que deseja comprar: ')

if produto_selecionado == 'produtos':

#regra de desconto

'''  A loja tem uma promoção. Antes de cobrar, se o valor original do item for maior que R$ 300,00,
aplique um desconto de 10%  '''