from time import sleep


def formatar_nome(nome):
    print(f'Formatando o nome "{nome}"...')
    sleep(3)
    return nome.title()


def genero_valido(genero: str) -> bool:
    todes = ['Transexual', 'Neutro']
    generos_validos = ['Masculino', 'Feminino', 'Fem', 'Masc', 'F', 'M'] + todes

    if genero.capitalize() in generos_validos:
        return True 
    else: 
        return False
    

def maior_de_idade(idade: int):
    if idade >= 18:  # > =
        return True
    else:
        return False


# pessoa = {
#     'nome': "ana zanatta",
#     'idade': 20,
#     'genero': "Feminino",
#     'altura': 1.60
# }

pessoas = []
while True:
    print('Cadastro de pessoas com gênero válido e maiores de idade')

    nome = formatar_nome(nome=input('Nome da pessoa: '))

    idade = int(input('Idade da pessoa: '))
    if not maior_de_idade(idade=idade):
        print('Menor de idade!!!!')
        continue

    genero = input('Gênero da pessoa: ')
    if not genero_valido(genero=genero):
        print('Gênero inválido!!!!')
        continue

    altura = float(input('Altura da pessoa: '))

    pessoa = {
        'nome': nome,
        'idade': idade,
        'genero': genero,
        'altura': altura     
    }

    pessoas.append(pessoa)

    if len(pessoas) > 4:
        break    

print(pessoas)