import csv


def csv_importer(path: str):
    with open(path, 'r', encoding='utf8') as data:
        data_list = csv.DictReader(data)
        readed_data = list(data_list)
    return readed_data
