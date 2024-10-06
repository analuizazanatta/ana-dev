"""lista = [1, 'A', True]

dicionario_1 = {
    'nome': 'Ana',
    'idade': 20
}  
# chave: valor

lista[0]  # 1
dicionario_1['nome']  # 'Ana'

# _________________________________
"""

# cachorro = {
#     "Nome": "Sun",
#     "Idade": 2,
#     "Raça": "Yorkshire",
#     "Pelagem": "Marrom",
#     "Castrado": False,
#     "TemTodasVacinas": "Não"
#     # "TemTodasVacinas": False
# }

# if cachorro["Idade"] > 1 and cachorro["TemTodasVacinas"] != "Não":  # cachorro["TemTodasVacinas"]:
#     print('Pode')

# cachorros = [
#     {
#         "Nome": "Sun",
#         "Idade": 2,
#         "Raça": "Yorkshire",
#         "Pelagem": "Marrom",
#         "Castrado": False,
#         "TemTodasVacinas": "Não"
#         # "TemTodasVacinas": False
#     },
#     {
#         "Nome": "Sun",
#         "Idade": 2,
#         "Raça": "Yorkshire",
#         "Pelagem": "Marrom",
#         "Castrado": False,
#         "TemTodasVacinas": "Não",
#         "VacinasTomadas": "Vermífogo;RaivaLoca;Tetano"
#         # "TemTodasVacinas": False
#     },
# ]

# cachorro = cachorros[1]

# # if "Raiva" in cachorro["VacinasTomadas"]:
# if "Raiva" in cachorro["VacinasTomadas"].split(";"):  # ["Vermífogo", "RaivaLoca", "Tetano"]
#     print('pode passear')
# else:
#     print('não pode passear')

cachorro = {
    "Nome": "Sun",
    "Raça": "Yorkshire",
    "Pelagem": "Marrom"
}

print(cachorro)

cachorro["Nome"] = "Tadeu"
print(cachorro)

cachorro["Vacinas"] = "SIM"
# print(cachorro["Vacinas"])
# print(cachorro["Alergia"])
print(cachorro.get("Vacinas", "N"))
print(cachorro.get("Alergia", "nao tem alergia"))
print(cachorro.get("Outro"))

# lista = [1, 'A', True]
# lista[0] = "blablabla"
# print(lista)
