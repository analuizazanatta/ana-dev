"""
O que é uma lista:
Em Python, uma lista é uma estrutura de dados que permite armazenar uma coleção ordenada de itens (elementos), 
que podem ser de tipos diferentes, como inteiros, strings, ou até mesmo outras listas. 
As listas são mutáveis, ou seja, você pode alterar, adicionar ou remover elementos após a criação da lista.

Como definir uma lista em Python:
Você define uma lista colocando os elementos entre colchetes [], separados por vírgulas.
"""

# Definindo uma lista de números inteiros
numeros = [1, 2, 3, 4, 5]

# Definindo uma lista com tipos diferentes de dados
mistura = [1, "texto", 3.14, True, [1], ["texto"], [3.14], [True], str, bool]

# Definindo uma lista vazia
vazia = []

"""
Acessando elementos de uma lista:
Os elementos de uma lista são indexados, começando do índice 0. 
Você pode acessar, modificar ou remover elementos usando esses índices.
"""

# Acessando o primeiro elemento
primeiro_elemento = numeros[0]  # Resultado: 1

# Acessando o último elemento
ultimo_elemento = numeros[-1]  # Resultado: 5

# Modificando um elemento
numeros[2] = 10  # Agora a lista é [1, 2, 10, 4, 5]

# Removendo um elemento
del numeros[1]  # Agora a lista é [1, 10, 4, 5]

"""
Operações comuns com listas:
Você pode realizar várias operações com listas, como adicionar elementos, concatenar listas, 
verificar se um elemento está na lista, entre outras.
"""

# Adicionando um elemento ao final da lista
numeros.append(6)  # Agora a lista é [1, 10, 4, 5, 6]

# Concatenando duas listas
mais_numeros = numeros + [7, 8]  # Resultado: [1, 10, 4, 5, 6, 7, 8]

# Verificando se um elemento está na lista
existe = 10 in numeros  # Resultado: True

# As listas são uma das estruturas de dados mais fundamentais em Python, 
# permitindo manipulações complexas de dados de forma eficiente e flexível.

# Operações da lista
lista = [1, 2, 3, 4, 5, 6]

lista.append(4)  # Adiciona o valor ao final - [1, 2, 3, 4, 5, 6, 4]
lista.insert(3, 4)  # Adiciona o valor no índice informado (adiciona o valor 4 no índice 3) - [1, 2, 3, 4, 4, 5, 6, 4]

lista.remove(4)  # Remove o valor (se tiver mais de 1, remove o com índice menor) - [1, 2, 3, 4, 5, 6, 4]
lista.pop()  # Remove o último valor - [1, 2, 3, 4, 5, 6]
lista.pop(0)  # Remove pelo índice - [2, 3, 4, 5, 6]

lista.index(5)  # 3 - Retorna o índice do valor (se não existir na lista, retorna -1)
lista.count(6)  # 1 - Retorna a quantidade de vezes que o valor aparece na lista