valor = float(input("Digite um valor: "))

#regra de negocio:
    # se a venda for ate 100 reais, de 5% de desconto
    #se a venda for entre 100 e 200 reais, de 10% de desconto
    #se a venda for acima de 300 reais, de 15% de descont


if valor <= 100:
    print("o valor da compra foi de: ", valor)
    exit()

elif valor > 100 and valor <= 299.00:
    desconto = 0.90
else:
    desconto = 0.85

total = valor * desconto
descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual)

print(f"Sua compra deu R${total:.2f} com um desconto de {descontoPercentual}%")


