# - Criar e excluir CATEGORIAS (nome)

categorias = []

def adicionar_nova_categoria(nome_categoria):
    if nome_categoria not in categorias: 
        categorias.append(nome_categoria)
    else:
        print('Categoria já existente!')

# Cria e adiciona CATEGORIA 
# while input('Deseja adicionar uma categoria? [S/N] ').upper() == 'S':
#     categoria = input('Digite o nome de uma nova CATEGORIA: ').capitalize()
#     adicionar_nova_categoria(nome_categoria=categoria)
    

# print(categorias)

# Para remover duplicados, pode-se utilizar esse código 
# categorias = list(set(categorias))  
# "set" é um conjunto de dados igual a lista mas NÃO ACEITA VALORES DUPLICADOS

def remover_categoria(nome_categoria):
    if nome_categoria in categorias: 
        categorias.remove(nome_categoria)
    else:
        print('Categoria não existente!')

# while input('Deseja remover uma categoria? [S/N] ').upper() == 'S':
#     categoria = input('Digite o nome da CATEGORIA: ').capitalize()
#     remover_categoria(nome_categoria=categoria)
    

# print(categorias)