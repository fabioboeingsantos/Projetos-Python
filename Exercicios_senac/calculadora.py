def somar(n1, n2):
    total = n1 + n2
    print(f"{n1} + {n2} = {total}")

def subtrair(n1, n2):
    total = n1 - n2
    print(f"{n1} - {n2} = {total}")

def multiplicar(n1, n2):
    total = n1 * n2
    print(f"{n1} x {n2} = {total}")

def dividir(n1, n2):
    if n2 == 0: print("Não é possível dividir por zero!")
    else: print(f"{n1} / {n2} = {round(n1 / n2, 2)}")

while True:
    menu = """
    ================================
    Calculadora:
    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (x)
    4 - Divisão (/)
    0 - Sair
    ================================
    """
    print(menu)
    opcao = input("Escolha uma opção acima e digite: ")

    if opcao == "0": 
        
        break

    if opcao not in ["1", "2", "3", "4", "0"]:
        print("Opção inválida! Tente novamente!")
        continue

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if opcao == "1": somar(n1, n2) 
    elif opcao == "2": subtrair(n1, n2)    
    elif opcao == "3": multiplicar(n1, n2)   
    elif opcao == "4": dividir(n1, n2)

     
    else:
        print("Opção Inválida!")   




print("Somando fora do while...")
somar(5, 5)







'''
def somar (n1, n2):
    total = n1 + n2
    print(f'Resultado: {n1} + {n2} = {total}')
    return total

def subtracao (n1, n2):
    total = n1 - n2
    print(f'Resultado: {n1} - {n2} = {total}')
    return total

def multiplicacao (n1, n2):
    total = n1 * n2
    print(f'Resultado: {n1} * {n2} = {total}')
    return total

def divisao (n1, n2):
    total = n1 / n2
    if n2 == 0: print('Nao e possivel dividir por 0')
    else: print(f'Resultado: {n1} / {n2} = {total}')
    return total



while True:
    print('='*23 )
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

    n1 = int(input('Digite o primeiro numero '))
    n2 = int(input('Digite o segundo numero '))

    if opcao == '1': # ULTILIZAR STRG SEMPRE QUANDO O MENU ESTIVER COMO STRING
        total = n1 + n2
        #print('total')
        print(f'Resultado: {n1} + {n2} = {total}')
    elif opcao == '2':
        total = n1 - n2
        print(f'Resultado: {n1} - {n2} = {total}')
        #print('total')
    elif opcao == '3':
        total = n1 * n2
        #print(total)
        print(f'Resultado: {n1} * {n2} = {total}')
    elif opcao == "4":
        total = {n1} / {n2}
        if n2 == 0: print('Nao e possivel dividir por 0')
        else: print(f'Resultado: {n1} / {n2} = {total}')

        
    print('\n' + '='*23 + '\n')


if opcao == '1': somar(n1, n2)
        
elif opcao == '2':subtracao(n1, n2)
                            
elif opcao == '3': multiplicacao(n1,n2)
                            
elif opcao == "4": divisao(n1, n2)



def somar(n1, n2):
    total = n1 + n2
    print(f"{n1} + {n2} = {total}")

def subtrair(n1, n2):
    total = n1 - n2
    print(f"{n1} - {n2} = {total}")

def multiplicar(n1, n2):
    total = n1 * n2
    print(f"{n1} x {n2} = {total}")

def dividir(n1, n2):
    if n2 == 0: print("Não é possível dividir por zero!")
    else: print(f"{n1} / {n2} = {round(n1 / n2, 2)}")

while True:
    menu = """
    ================================
    Calculadora:
    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (x)
    4 - Divisão (/)
    0 - Sair
    ================================
    """
    print(menu)
    opcao = input("Escolha uma opção acima e digite: ")

    if opcao == "0": 
        
        break

    if opcao not in ["1", "2", "3", "4", "0"]:
        print("Opção inválida! Tente novamente!")
        continue

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if opcao == "1": somar(n1, n2) 
    elif opcao == "2": subtrair(n1, n2)    
    elif opcao == "3": multiplicar(n1, n2)   
    elif opcao == "4": dividir(n1, n2)

     
    else:
        print("Opção Inválida!")   




print("Somando fora do while...")
somar(5, 5)

'''