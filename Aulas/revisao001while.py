
'''usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')'''

usuario_correto = 'admin'
senha_correta = '1234'

usuario = ''
senha = ''
'''continuar = 'sim'
nao_continuar = 'nao'''


while usuario != usuario_correto or senha != senha_correta:
    usuario = input('Digite seu usuario: ')
    senha = input('digite sua senha: ')
    
    if usuario != usuario_correto or senha != senha_correta:
        print('usuario e senha incorreto, tente novamente')
    else:
        print('acesso permitido')