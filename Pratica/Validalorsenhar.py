'''
Problema: 
Voce trabalha em um sitema que precisa verificar se todas as senhas digitadas por usuarios sao validas.
Para uma senha ser valida ela precisa ter pelo menos 6 caracteres.

Quais os dados de entrada? 
- senha

O que fazer com os dados? 
-verificar se possui minimo 6 caracter

Quais são as restrições? 
- e obrigado informar uma senha
- a senha deve possuir minimo 6 caracteres

Qual é o resultado esperado? 
-se a senha informada tiver menos que 6 caracteres, nao permitir o uso
- se a senha informada tiver 6 ou mais, permitir uso

Qual a sequência de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
- receber senha
- verficar se ela tem o mino 6 caracter
- se possuir, permitir, se nao, nao permitir

'''


#senhas = ['abc', 'segura123', '123456', 'oi']
#for senha in senhas:
 #   if len(senha):
    #    print(f' a senha{senha} e valida')

  #  else:
   #     print (f' A senha {senha} deve possuir no minimo 6 caracter')


#LEN(usado para quantidade de caracteres). 

#CRIAR UM PROGRAMA QUE PERMITE 3 TENTATIVAS, ANTES DE FECHAR
tentativas = 0
while tentativas <=3:
    print('Tente novamente')
    tentativas = tentativas + 1

#quando queremos que uma acao continue acontecendo, ate que um criterio seja satisfeito
#so pode logar, se digitar a senha certa.

senha = ""

while senha != "123456":
    senha = input('Digite a senha: ')
    
    if senha != "123456":
        print('Senha incorreta, tente novamente.')

print('Bem-vindo! Acesso liberado.')



















