from inventory_report.inventory.product import Product


def test_cria_produto():
    values_dict = {
        'prod_id': 1,
        'nome': 'Produto',
        'empresa': 'Empresa',
        'frabricacao': '11/11/1111',
        'validade': '22/22/2222',
        'numero_serie': '40028922',
        'armazenamento': 'Deixar exposto ao sol sem proteção'
    }
    produto = Product(values_dict['prod_id'],
                      values_dict['nome'],
                      values_dict['empresa'],
                      values_dict['frabricacao'],
                      values_dict['validade'],
                      values_dict['numero_serie'],
                      values_dict['armazenamento'])

    assert produto.id == values_dict['prod_id']
    assert produto.nome_do_produto == values_dict['nome']
    assert produto.nome_da_empresa == values_dict['empresa']
    assert produto.data_de_fabricacao == values_dict['frabricacao']
    assert produto.data_de_validade == values_dict['validade']
    assert produto.numero_de_serie == values_dict['numero_serie']
    assert produto.instrucoes_de_armazenamento == values_dict['armazenamento']
