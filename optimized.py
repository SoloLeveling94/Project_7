from datetime import datetime
import csv


def import_csv(file):
    try:
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            tab_import_csv = []

            for row in csv_reader:
                net_profit = float(row["price"]) * float(row["profit"]) / 100
                dict_csv = {"name": row["name"], "price": float(row["price"]), "profit":
                    float(row["profit"]), "net profit": net_profit}
                tab_import_csv.append(dict_csv)
        return (tab_import_csv)

    except OSError:
        print(f'Could not open/read file: {file}')

def price(action):
    return action['price']


def net_profit(action):
    return action['net profit']


def profit(action):
    return action['profit']


def total_price(tab):
    t_price = 0
    for action in tab:
        t_price += action['price']

    return t_price


def total_net_profit(tab):
    t_net_profit = 0
    for action in tab:
        t_net_profit = action['net profit']

    return t_net_profit


def algo_glouton(tab, price_max):
    tab_tried = sorted(tab, key=profit, reverse=True)
    total_price = 0
    total_net_profit = 0
    solution_glouton = []

    for action in tab_tried:
        if total_price + action['price'] <= price_max and action['price'] > 0:
            total_price += action['price']
            total_net_profit += action['net profit']
            solution_glouton.append(action)

    return total_price, total_net_profit, solution_glouton


tab_import_csv = import_csv('brute.csv')
tab_tried = sorted(tab_import_csv, key=net_profit, reverse=True)

start_time = datetime.now()
print(algo_glouton(tab_import_csv, 500))
end_time = datetime.now()
print('time glouton -> {}'.format(end_time - start_time))

