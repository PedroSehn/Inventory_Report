from datetime import datetime


def oldest_fabrication(list: list):
    menor_data = datetime(2029, 10, 12)
    for i in list:
        date = datetime.strptime(i['data_de_fabricacao'], ("%Y-%m-%d"))
        if date < menor_data:
            menor_data = date
    return menor_data.date()
