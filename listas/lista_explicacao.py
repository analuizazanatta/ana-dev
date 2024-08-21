# Como remover todas as ocorrências de um item na lista

lista = [1, 2, 3, 4, 4, 5, 6, 4, 7, 4, 8, 9, 4]

count = lista.count(4)
for _ in range(count):
    lista.remove(4)

while True:
    index = lista.index(4)

    if index == -1:
        break
    
    lista.pop(index)
