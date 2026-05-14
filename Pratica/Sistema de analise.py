'''
Desafio: Sistema de Análise de Turma

Você deve criar um programa que analisa o desempenho de uma turma de alunos com base em suas notas.

📌 Descrição do problema

O programa deverá:

Perguntar quantos alunos existem na turma
Para cada aluno, solicitar:
Nome
Nota (de 0 a 10)
Armazenar essas informações (você decide como: listas, dicionários, etc.)
⚙️ Regras de classificação (condicionais obrigatórias)

Para cada aluno, classifique:

Nota ≥ 7 → Aprovado
Nota entre 5 e 6.9 → Recuperação
Nota < 5 → Reprovado
🔁 Requisitos com for
Use um for para percorrer todos os alunos cadastrados
Durante esse loop, você deve:
Exibir o resultado individual de cada aluno
Contabilizar:
Quantos foram aprovados
Quantos estão em recuperação
Quantos foram reprovados
📊 Relatório final (obrigatório)

Após o loop, o programa deve mostrar:

Total de alunos
Quantidade em cada categoria
Percentual de cada categoria (ex: 40% aprovados)
🔥 Desafio extra (nível difícil mesmo)

Durante o for, implemente também:

Identificar e mostrar:
O aluno com maior nota
O aluno com menor nota
🚫 Regras importantes
Validar a nota (não permitir valores menores que 0 ou maiores que 10)
Se a nota for inválida, pedir novamente (pode usar while dentro do for)
Organizar bem a saída (legível no terminal)
💡 Dica

Tente separar a lógica em partes:

Entrada de dados
Processamento
Saída final

'''
lista_de_nomes = []
lista_de_notas = []

contador_de_aprovados = 0
contador_de_recuperacao = 0
contador_de_reprovados = 0


maior_nota_da_turma = 0 
nome_do_melhor_aluno = ""


quantidade_de_alunos = int(input("Quantos alunos você deseja cadastrar? "))

# O 'range' cria uma sequência de números para o loop seguir (Ex: se for 3, ele faz 0, 1, 2)
for posicao in range(quantidade_de_alunos):
    nome_do_aluno = input("Digite o nome do aluno: ")
    nota_do_aluno = float(input("Digite a nota do aluno (Use ponto em vez de vírgula): "))
    
    # O 'append' coloca o que foi digitado no final da lista (Como adicionar uma linha nova)
    lista_de_nomes.append(nome_do_aluno)
    lista_de_notas.append(nota_do_aluno)
    
    # Testando se a nota atual é a maior encontrada até agora
    if nota_do_aluno > maior_nota_da_turma:
        maior_nota_da_turma = nota_do_aluno
        nome_do_melhor_aluno = nome_do_aluno

# --- PASSO 3: Analisando e exibindo os resultados (O processamento) ---
print("\n--- RESULTADOS INDIVIDUAIS ---")

# O 'enumerate' entrega a posição e o conteúdo da lista ao mesmo tempo
for posicao, nome_atual in enumerate(lista_de_nomes):
    # Usamos a 'posicao' para pegar a nota correta na outra lista (Sincronização)
    nota_atual = lista_de_notas[posicao]
    
    # Condicionais para decidir o status (O 'elif' é uma alternativa ao 'if' anterior)
    if nota_atual >= 7:
        situacao_final = "Aprovado"
        contador_de_aprovados = contador_de_aprovados + 1
        
    elif nota_atual >= 5:
        situacao_final = "Recuperação"
        contador_de_recuperacao = contador_de_recuperacao + 1
        
    else:
        situacao_final = "Reprovado"
        contador_de_reprovados = contador_de_reprovados + 1
        
    # Exibindo os dados (A vírgula no print junta textos e números automaticamente)
    print("O aluno", nome_atual, "tirou nota", nota_atual, "e sua situação é:", situacao_final)

# --- PASSO 4: Relatório Final (A matemática final do programa) ---
# O 'sum' soma todos os números que estão dentro da lista de notas
soma_total_das_notas = sum(lista_de_notas)
media_geral_da_turma = soma_total_das_notas / quantidade_de_alunos

# Cálculo de porcentagem (Parte dividida pelo todo, vezes cem)
porcentagem_de_aprovacao = (contador_de_aprovados / quantidade_de_alunos) * 100

print("\n--- RESUMO GERAL DA TURMA ---")
print("Média final da turma:", media_geral_da_turma)
print("Melhor aluno da turma:", nome_do_melhor_aluno, "(Nota:", maior_nota_da_turma, ")")
print("Total de aprovados:", contador_de_aprovados)
print("Total em recuperação:", contador_de_recuperacao)
print("Total de reprovados:", contador_de_reprovados)
print("Taxa de aprovação:", porcentagem_de_aprovacao, "%")
