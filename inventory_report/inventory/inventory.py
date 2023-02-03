from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import csv_importer
from inventory_report.importer.json_importer import json_importer
from inventory_report.importer.xml_importer import xml_importer


class Inventory:

    def simple_complex(type, clear_data):
        if type == 'simples':
            return SimpleReport.generate(clear_data)
        elif type == 'completo':
            return CompleteReport.generate(clear_data)

    def import_data(path: str, type: str):
        if '.csv' in path:
            clear_data = csv_importer(path)
            print(clear_data)
            return Inventory.simple_complex(type, clear_data)

        elif '.json' in path:
            clear_data = json_importer(path)
            return Inventory.simple_complex(type, clear_data)

        elif '.xml' in path:
            clear_data = xml_importer(path)
            return Inventory.simple_complex(type, clear_data)


Inventory.import_data = staticmethod(Inventory.import_data)
