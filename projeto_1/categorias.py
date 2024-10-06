# - Criar e excluir CATEGORIAS (nome)

categorias = []

# Cria e adiciona CATEGORIA 
while input('Deseja adicionar uma categoria? [S/N] ').upper() == 'S':
    categoria = input('Digite o nome de uma nova CATEGORIA: ').capitalize()
    
    if categoria not in categorias: 
        categorias.append(categoria)
    else:
        print('Categoria já existente!')

print(categorias)

# Para remover duplicados, pode-se utilizar esse código 
# categorias = list(set(categorias))  
# "set" é um conjunto de dados igual a lista mas NÃO ACEITA VALORES DUPLICADOS

while input('Deseja remover uma categoria? [S/N] ').upper() == 'S':
    categoria = input('Digite o nome da CATEGORIA: ').capitalize()
    
    if categoria in categorias: 
        categorias.remove(categoria)
    else:
        print('Categoria não existente!')

print(categorias)