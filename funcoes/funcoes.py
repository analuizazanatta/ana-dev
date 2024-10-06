
categorias = ['BLABLABLA']

def manipular_categorias():
    categorias = []

    # Adicionar
    while input('Deseja adicionar uma categoria? [S/N] ').upper() == 'S':
        categoria = input('Digite o nome de uma nova CATEGORIA: ').capitalize()
        
        if categoria not in categorias: 
            categorias.append(categoria)
        else:
            print('Categoria já existente!')

    # Excluir
    while input('Deseja remover uma categoria? [S/N] ').upper() == 'S':
        categoria = input('Digite o nome da CATEGORIA: ').capitalize()
        
        if categoria in categorias: 
            categorias.remove(categoria)
        else:
            print('Categoria não existente!')

    return categorias
