from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
data_path = '../data/inventory.csv'


class Inventory:
    def import_data(path: str, type: str):
        with open(path, 'r', encoding='utf8') as data:
            data_list = csv.DictReader(data)
            readed_data = list(data_list)
        if type == 'simples':
            return SimpleReport.generate(readed_data)
        else:
            return CompleteReport.generate(readed_data)


Inventory.import_data = staticmethod(Inventory.import_data)
