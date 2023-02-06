import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if '.xml' not in path:
            raise ValueError('Arquivo inválido')
        else:
            with open(path) as file:
                data = xmltodict.parse(file.read())['dataset']['record']
                return data


XmlImporter.import_data = staticmethod(XmlImporter.import_data)

# def xml_importer(path: str):
    # with open(path) as file:
        # data = xmltodict.parse(file.read())['dataset']['record']
        # return data
