
while True:
   
    print('===== Calculadora =====')
    
    menu = '''
    1 - Somar (+)
    2 - Subtracao (-)
    3 - Multiplicacao (*)
    4 - Divisao (/)
    0 - SAIR
    '''
    print(menu)

    opcao = (input('Digite a opcao desejada: '))
    
    if opcao == "0": 
        print('Saindo. ')
        break
    
    if opcao not in('1','2','3','4'):
       print('opcao invalida, tente novamente')  
       continue   # Volta para o início do "while", ignorando as linhas abaixo   

    n1 = int(input('Digite o primeiro numero'))
    n2 = int(input('Digite o segundo numero'))

    if opcao == '1': # ULTILIZAR STRG SEMPRE QUANDO O MENU ESTIVER COMO STRING
        total = n1 + n2
        #print('total')
        print(f'Resultado: {n1} + {n2} = {total}')
    elif opcao == '2':
        total = n1 - n2
        print(f'Resultado: {n1} + {n2} = {total}')
        #print('total')
    elif opcao == '3':
        total = n1 * n2
        #print(total)
        print(f'Resultado: {n1} * {n2} = {total}')
    #elif opcao == "4":
        if n2 == 0: print('nao e possivel dividir')
        else: print(f'Resultado: {n1} / {n2} = {total}')