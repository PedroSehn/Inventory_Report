from datetime import datetime


def sooner_expiration(list: list):
    now = datetime.now()
    date_list = []
    for item in list:
        val = datetime.strptime(item['data_de_validade'], ("%Y-%m-%d"))
        if (val > now):
            date_list.append(val)
    return min(date_list).date()
