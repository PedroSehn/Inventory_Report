mock = [
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 2,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 3,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Zoios",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
    {
        "id": 1,
        "nome_do_produto": "MESA",
        "nome_da_empresa": "Pedro's",
        "data_de_fabricacao": "2022-05-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
    },
]


def items_per_company(list: list):
    companies_dict = {}
    for item in list:
        company_name = item['nome_da_empresa']
        if item['nome_da_empresa'] not in companies_dict.keys():
            companies_dict[f'{company_name}'] = 1
        else:
            companies_dict[f'{company_name}'] += 1
    return companies_dict
