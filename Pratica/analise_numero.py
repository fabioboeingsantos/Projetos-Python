# 1. Preparação
numeros = []
pares = 0
impares = 0

# Entrada de dados
quantidade = int(input("Quantos números deseja digitar? "))

# 2. Primeiro laço 'for' para preencher a lista
for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# 3. Segundo laço 'for' para análise (lógica manual)
maior = numeros[0] # Começamos assumindo que o primeiro é o maior

for n in numeros:
    # Verificando se é par ou ímpar
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verificando o maior número (sem usar max())
    if n > maior:
        maior = n

# 4. Exibindo os resultados
print("-" * 30)
print(f"Lista completa: {numeros}")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"O maior número digitado: {maior}")
print("-" * 30)