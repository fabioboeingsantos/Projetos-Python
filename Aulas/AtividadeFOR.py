frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"] 
#lembrando que a posição do indice começa em 0, ou seja, maçã é a posição 0, banana é a posição 1 e assim por diante.
#entra do usuario a fruta favorita

fruta_favorita = input("Qual é a sua fruta favorita? ")
if fruta_favorita not in frutas:
    print("Desculpe, essa fruta não está na lista.")
    exit()
    #se a fruta favortira do usuario nao estiver na lista, imprima uma mensagem de erro e encerre o programa.

#para cada posicao(indice) e fruta na lista frutas, faca:
for posicao,fruta in enumerate(frutas):    
    #se a fruta dessa interacao e igual a fruta favorita do usuario, faca:

    if fruta == fruta_favorita:
        #salva em uma variavel a posicao da fruta favorita do usuario

        posicao_fruta_favorita = posicao        
        break
print(f"minha fruta favorita é a {fruta_favorita} e ela está na posição {posicao_fruta_favorita} da lista.")

#saida com algoritmo print.


