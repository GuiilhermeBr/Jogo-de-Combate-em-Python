inventario = [{
    'Armadura de Couro': 10,
    'Armadura de Malha': 15,
    'Armadura de Aço': 25,
    'Armadura de Placas de Ferro': 40
}]

# Acessando o primeiro item do dicionário
primeiro_item = inventario[0]  # Acessa o primeiro dicionário na lista
nome_armadura = list(primeiro_item.keys())[0]  # Nome da primeira armadura
valor_armadura = primeiro_item[nome_armadura]  # Valor da primeira armadura

for x in inventario[0]:
    print(x)