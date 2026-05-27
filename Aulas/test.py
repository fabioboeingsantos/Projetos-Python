# ==========================================
# ETAPA 1: CONFIGURAÇÃO DOS DADOS (VARIÁVEIS)
# ==========================================
produtos = ['Pneu', 'Bateria', 'Óleo', 'Palheta']
servicos = ['Alinhamento', 'Revisão', 'Lavagem_completa', 'polimento']

preco_produtos = [430.99, 490.99, 149.99, 95.99]
# Correção: 350.00 com ponto para o Python reconhecer como número decimal
preco_servicos = [55.99, 399.99, 40.99, 350.00]


# ==========================================
# ETAPA 2: PRIMEIRO MENU (ESCOLHA DA CATEGORIA)
# ==========================================
# O .strip().lower() evita erros se o usuário digitar espaços ou letras maiúsculas
servico_produto_selecionado = input('"Você deseja ver nossos Produtos ou Servicos?"').strip().lower()

if servico_produto_selecionado == 'produtos':
    for posicao, produto in enumerate(produtos):
        print(f'{posicao + 1} - {produto} - R$: {preco_produtos[posicao]}.')

elif servico_produto_selecionado == 'servicos':
    for posicao, servico in enumerate(servicos):
         print(f'{posicao + 1} - {servico} - R$: {preco_servicos[posicao]}.')
else:
    print('Opção inválida. Digite "produtos" ou "servicos".')
    exit()  # Bloqueia o programa aqui se a categoria estiver errada


# ==========================================
# ETAPA 3: SEGUNDO MENU (ESCOLHA DO ITEM)
# ==========================================
numero_selecionado = int(input('Digite o número do item que deseja comprar: '))
indice = numero_selecionado - 1


# ==========================================
# ETAPA 4: PROCESSAMENTO LOGICO (DESCONTO)
# ==========================================
# Variáveis universais de suporte que vão alimentar o cupom lá no final
item_comprado = ""
preco = 0.0
preco_cheio = 0.0

# 1ª Barreira: Bloqueia números menores que zero ou maiores que o tamanho das listas
if numero_selecionado <= 0 or numero_selecionado > len(produtos) or numero_selecionado > len(servicos):
     print(f'Opcao invalida, Digite o numero de acordo com o produto, entre 1 e {len(produtos)}.')
     exit()

# 2ª Barreira: Se o número for válido, processa produtos
elif servico_produto_selecionado == 'produtos':
    item_comprado = produtos[indice]
    preco = preco_produtos[indice]
    preco_cheio = preco  # Tira uma "foto" do preço original antes de mexer nele
    
    if preco > 300:
        preco = preco * 0.9

# 3ª Barreira: Se o número for válido, processa serviços
elif servico_produto_selecionado == 'servicos':
    item_comprado = servicos[indice]
    preco = preco_servicos[indice]
    preco_cheio = preco  # Tira uma "foto" do preço original antes de mexer nele

    if preco > 300:
        preco = preco * 0.9


# ==========================================
# ETAPA 5: O IMPRESSOR DO CUPOM FISCAL
# ==========================================
print('\n' + '*' * 35)
print('Auto Peças e Oficina')
print('Blumenau - SC')
print('27/05/2026')
print('          CUPOM FISCAL          ')
print('-' * 35)
print('Item                         Valor')

# Exibe o item correto mapeado e o preço cheio original alinhado à direita
print(f'{item_comprado:<20} R$ {preco_cheio:>10.2f}')

# Se o preço atual for menor que o preço cheio, calcula e injeta a linha de desconto
if preco < preco_cheio:
    desconto_em_reais = preco_cheio - preco
    print(f'DESCONTO (10%)        -R$ {desconto_em_reais:>10.2f}')

print('-' * 35)

# Mostra o valor que realmente vai sair do bolso do cliente
print(f'TOTAL A PAGAR         R$ {preco:>10.2f}')
print('*' * 35)