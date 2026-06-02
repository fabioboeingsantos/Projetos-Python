def calcular_media(notas: list) ->float:
    media = sum(notas) / len(notas)
    return media

contador = 1
notas = []

while True:
    notas = float(f'Digite a nota {contador} ou "sair" para sair')
    notas.append(notas)
    print('Nota foi registrada')
    if notas == "sair":
        break    
        
def consumo(distancia, litros):
    return distancia / litros

def consumo(distancia, litros):
    if litros == 0:
        return "Litros não pode ser zero"
    return distancia / litros
