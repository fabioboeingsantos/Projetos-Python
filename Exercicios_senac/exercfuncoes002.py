def menu_simples ():
    print('='*30 )
    print(f'{"Conversor de unidades":^30}')
    print('='*30 )
    print("""
    1 - Celsius - fahrenheit 
    2 - Reais - Dolar
    3 - Horas - minutos
    0 - SAIR    
    """)
    print('='*30 )

def celsius_para_fahrenheit():
    celsius = float(input('Digite a temperatura em Celsius: '))
    fh = (celsius * 9/5) + 32
    print(f'{celsius}°C é igual a {fh}°F')

def reais_para_dolar():
    reais = float(input('Digite o valor em Reais: '))
    reais_para_dolar = reais / 5
    print(f'{reais} é igual a {reais_para_dolar} Dólares')

def horas_para_minutos():
    horas = float(input('Digite o valor em Horas: '))
    minutos = horas * 60
    print(f'{horas} é igual a {minutos} minutos')

while True:
    menu_simples()
    opcao = input('Escolha uma opção: ')
    
    if opcao == '0':
        print('Saindo.')
        break

    elif opcao == '1':
        celsius_para_fahrenheit()

    elif opcao == '2':
        reais_para_dolar()

    elif opcao == '3':
        horas_para_minutos()

    else:
        print('Opção inválida')



