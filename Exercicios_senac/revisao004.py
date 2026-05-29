compras = ['camisa','calca', 'bermuda,']

compras.append('cueca')

print(compras[0])

compras.append('toca')

print(compras[3])

print(len(compras)) # esta contando a quantidade de itens.

print(compras)

compras.remove('calca')
print(compras)

numeros = [5,4,5,6,9]
total = sum(numeros)
print({total})

quantidade = len(compras)

if quantidade >= 4:
    print('Total')
else:
    print('Insira mais elementos')