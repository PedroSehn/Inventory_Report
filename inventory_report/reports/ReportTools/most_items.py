
def most_items(list: list):
    empresas = []
    for i in list:
        empresas.append(i['nome_da_empresa'])
    return max(set(empresas), key=empresas.count)
