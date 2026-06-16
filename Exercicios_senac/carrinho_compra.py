

''' Os produtos ficam numa lista de objetios, Produto, crie manu while true, permite adicionar item e verr toral de compra.
(1) adicionar produto
(2) listar item e dar o total
(3) filtrar por setor
(0) sair

Dica:   - A classe produto guarda nome, preco e setor.
        - guarde tudo em uma lista "CARRINHO = []"
        - total: for p in carrinho: total += p.preco.
        - mostre o dinheiro com R$
        - liste numerado com enumerate(carrinho, 1)
'''

from turtle import setworldcoordinates


class Produto():
    def __init__(self, nome: str, preco: float, setor: str):
        self.nome = nome
        self.preco = preco
        self.setor = setor
    
    def exibir(self):        
        print(f'Nome: {self.nome}, preco: {self.preco}, setor: {self.setor} ')


def menu_carrinho():
    print('='*30)
    print(f'\n{"Carrinho de compras":^30}')
    print(f'\n(1) - Adicionar produto')
    print('(2) - Listar item e dar o total')
    print('(3) - Filtrar por setor')
    print('(0) - Sair')
    print('\n' +'='*30)

def adicionar_produto():
    print('\nAdicionando produto')
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco do produto: '))
    setor = input('Digite o setor do produto: ')
    novo_produto = Produto(nome, preco, setor)
    carrinho.append(novo_produto)
    print(f'Produto {nome} adicionado com sucesso')


def listar_item_e_total():
    print('\nListando item e total')
    total = 0
    for posicao, produto in enumerate(carrinho):
        print(f'{posicao + 1} - {produto.nome} - R$ {produto.preco}')
        total += produto.preco
    print(f'Total: R$ {total}')
    indice = carrinho
    produto = carrinho[indice]

def filtrar_por_setor():
    setor = input('Digite o setor do produto: ')

    for posicao, produto in enumerate(carrinho):
        if produto.setor == setor:
            print(f'{posicao + 1} - {produto.nome} - {produto.preco}')
    produto.exibir()
    
carrinho = []

while True:
    menu_carrinho()
    opcao = input('Digite sua opcao de acordo com o menu')

    if opcao == 0:
        break

    if opcao == 1:
        adicionar_produto()

    if opcao == 2:
        listar_item_e_total()

    if opcao == 3:
        filtrar_por_setor()

    




