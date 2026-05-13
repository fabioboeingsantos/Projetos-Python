
usuario = ''
senha = ''
tentativas = 0 

while (usuario != 'fabio' or senha != 'senha123' and tentativas < 3):
    usuario = input('digite sua senha')
    senha = input('digite sua senha')
    tentativas = tentativas + 1 # Opcao de codigo menor, tentativas += 1 

if usuario == 'fabio' and senha == 'senha': 
    print('login feito com sucesso')
else:
    print('favor aguardar 30 min')
