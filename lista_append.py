# adiciona frutas através de um input

fruta = []

for i in range(3):

    x = input(f'Digite o nome da {i+1}ª fruta: ')
    # {i+1}ª é para a formatação na hora de imprimir, sair como "Digite o nome da 1ª fruta"
    
    fruta.append(x)
print(f'Lista de frutas {fruta}')
# [-1] serve para imprimir o último ítem da lista 
print(fruta[-1])