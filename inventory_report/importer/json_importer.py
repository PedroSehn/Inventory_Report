import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if '.json' not in path:
            raise ValueError('Arquivo inválido')
        else:
            with open(path) as file:
                data = json.loads(file.read())
                return list(data)


JsonImporter.import_data = staticmethod(JsonImporter.import_data)
