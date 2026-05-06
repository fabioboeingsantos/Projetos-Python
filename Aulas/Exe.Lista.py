mercado = ['arroz', 'feijão', 'macarrão', 'carne', 'frango']
mercado = [mercado[0], mercado[1], mercado[2], mercado[3], mercado[4]]
print(mercado[4]) 
print(mercado[0], mercado[1], mercado[2], mercado[3])
print(len(mercado))
print(mercado)

#segunda ativade

mercado_preco = ['3.5', '5', '4', '5.5', '8.0']
print(mercado_preco[0])

mercado.remove ('frango')
print('você removeu o item: frango')

total = float(mercado_preco[0]) + float(mercado_preco[1]) + float(mercado_preco[2]) + float(mercado_preco[3]) + float(mercado_preco[4])
print ('o valor total da compra é: R$', total)

if total >= 20:
    print('o valor total da compra é: R$', total, 'você tem direito a um desconto de 5%')
     
desconto = total * 0.95
print('o valor total da compra com desconto é: R$', desconto)

valordesconto = round(total - desconto, 2)
print('o valor do desconto é: R$', valordesconto)











                                                                                                                      




