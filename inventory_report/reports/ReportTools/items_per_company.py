
def items_per_company(list: list):
    companies_dict = {}
    for item in list:
        company_name = item['nome_da_empresa']
        if item['nome_da_empresa'] not in companies_dict.keys():
            companies_dict[f'{company_name}'] = 1
        else:
            companies_dict[f'{company_name}'] += 1
    return companies_dict
