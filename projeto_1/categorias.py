# - Criar e excluir CATEGORIAS (nome)

categorias = []


def adicionar_nova_categoria(nome_categoria):
    if nome_categoria not in categorias: 
        categorias.append(nome_categoria)
    else:
        print('Categoria já existente!')


def remover_categoria(nome_categoria):
    if nome_categoria in categorias: 
        categorias.remove(nome_categoria)
    else:
        print('Categoria não existente!')
