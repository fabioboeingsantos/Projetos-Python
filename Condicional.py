valor = float(input("Digite um valor: "))

#regra de negocio:
    # se a venda for ate 100 reais, de 5% de desconto
    #se a venda for entre 100 e 200 reais, de 10% de desconto
    #se a venda for acima de 300 reais, de 15% de desconto


if valor >= 100:
    desconto = 0.95
    #total = valor * desconto
#   valor = valor * 0.95
#  print("Valor com desconto: ", valor)     

elif valor > 100 and valor <= 299.00:
    desconto = 0.90
   # total = valor * desconto
 #   print("Valor com desconto: ", valor)

else:
    desconto = 0.85
    #total = valor * desconto
 #   print("Valor total foi de: ", total)

total = valor * desconto
#print("Valor com desconto: ", total)

descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual)
#print("valor total foi de: ", total)
#print("o valor do desconto foi de: ", descontoPercentual, "%")

print(f"Sua compra deu R${total:.2f} com um desconto de {descontoPercentual}%")

















   

