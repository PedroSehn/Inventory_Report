import xmltodict


def xml_importer(path: str):
    with open(path) as file:
        data = xmltodict.parse(file.read())['dataset']['record']
        return data
