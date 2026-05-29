'''for i in range(10):
    print(i)

for i in range(10,22,2):
    print(i)

for tabuada in range(5,55,5):   #tabuada 5
    print(tabuada)'''

for multiplicador in range(1, 11):
    resultado = multiplicador * 5
    print(f'{multiplicador} x 5 = {resultado}')

cidades = ['indaial','blumenau','gaspar','ilhota']
for cidade in (cidades):
    
    if cidade[0] == "B":
        continue
    print(cidade)
    #else:
       # print(cidade)
