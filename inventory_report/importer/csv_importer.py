import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if '.csv' not in path:
            raise ValueError('Arquivo inválido')
        else:
            with open(path, 'r', encoding='utf8') as data:
                data = list(csv.DictReader(data))
            return data


CsvImporter.import_data = staticmethod(CsvImporter.import_data)


# def csv_importer(path: str):
    # with open(path, 'r', encoding='utf8') as data:
        # data_list = csv.DictReader(data)
        # readed_data = list(data_list)
   # return readed_data
