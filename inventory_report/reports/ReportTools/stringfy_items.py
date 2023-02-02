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


def stringfy_items(dict: dict):
    companies_dict = {"Forces of Nature": 2, "Zoios": 1, "Pedro's": 1}
    keys = companies_dict.keys()
    string_list = []

    for key in keys:
        value = companies_dict[f"{key}"]
        string_list.append(f"- {key}: {value}\n")
    return "".join(string_list)
