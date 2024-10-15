
# Sistema de despesas

# - [OK] Criar e excluir CATEGORIAS (nome)
# - Criar e excluir PESSOAS (nome e saldo)
# - Criar e excluir DESPESAS (nome, valor, data, categoria, pagador[pessoa])

# Usar dicionários e listas para organizar e manipular os dados
# + Aprender o que é, como usar e onde usar FUNÇÕES


from categorias import adicionar_nova_categoria, remover_categoria, categorias

while True:
    print('1. Adicionar categoria')
    print('2. Remover categoria')

    pergunta = input('Deseja fazer o que? ')

    if pergunta == '1':
        categoria = input('Digite um nome de categoria: ')
        adicionar_nova_categoria(nome_categoria=categoria)
    elif pergunta == '2':
        categoria = input('Digite um nome de categoria: ')
        remover_categoria(nome_categoria=categoria)
    else:
        print('Opção inválida')

    print(categorias)