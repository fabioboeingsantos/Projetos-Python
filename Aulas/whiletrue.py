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

    opcao = int(input('Digite a opcao desejada'))
    if opcao == "0": 
    
    if opcao not in('1','2','3','4'):
       print('opcao invalida, tente novamente')
        break


    n1 = int(input('Digite o primeiro numero'))
    n2 = int(input('Digite o segundo numero'))

    if opcao == '1':
        total = n1 + n2
        print('total')
    elif opcao == '2':
        total = n1 - n2
        print('total')
    elif opcao == '3':
        total = n1 * n2
        print(total)
    elif opcao == "4":
        if n2 == 0: print('nao e possivel dividir')
        else: print(f'{n1}) - {n2} =
