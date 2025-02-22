import csv

from data import DATA


def add_item(ids, names, hrefs, prices, old_prices):
    for i in range(len(ids)):
        DATA.append([ids[i], names[i], hrefs[i], prices[i], old_prices[i]])


def write_item(city, center):
    with open(f'/{city}/data_{center}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Запись данных в файл
        for row in DATA:
            writer.writerow(row)
    DATA.clear()
