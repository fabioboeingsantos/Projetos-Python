#variáveis
nome = "Alice"
idade = 30
print(f"Nome: {nome}, Idade: {idade}")

#controlar o fluxo(if, else, elif)
nota = float(input("Digite sua nota: "))
if nota >= 7:
    print("Aprovado")   
elif nota >= 5:
    print("Recuperação")
else:    print("Reprovado")

#listas
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Acessa a primeira fruta
frutas.append("uva")  # Adiciona uma nova fruta
print(frutas)
# frutas = [`5',true, 20.5, "texto"] # lista heterogênea

#laco de repetição for e while
#for i in range(5):


#categorize os salarios:
#laco de repetição for:
salarios = [1500, 2500, 3500, 4500, 5500]
#se salario for menor que ou igual a 2000, baixo
#se salario for maior que 2000 e menor ou igual a 4000, medio
#se salario for maior que 4000, alto
for salario in salarios:
    if salario <= 2000:
        print(f"Salário: {salario} - Baixo")
    elif salario <= 4000:
        print(f"Salário: {salario} - Médio")
    else:
        print(f"Salário: {salario} - Alto")
        
