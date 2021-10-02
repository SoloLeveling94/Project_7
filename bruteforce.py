from itertools import combinations
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


def bruteForce(tab, price_max,  combinaisons=[]):
    for i in range(0, len(tab)):
        combinaisons.append([n for n in list(combinations(tab, i))])

    max_profit = 0
    for combi in combinaisons:
        for liste in combi:
            price = 0
            profit = 0
            for k in liste:
                price += k.get('price')
                profit += k.get('net profit')
            if max_profit < profit and price <= price_max:
                max_profit = profit
                actions = liste
                prix = price

    return (max_profit, prix, actions)


def algo_sac_a_dos(tab, price_max):
    n = len(tab)
    tab_entiers = [i for i in range(2 ** n)]
    tab_binaire = [bin(i)[2:] for i in tab_entiers]
    combinaisons = ['0' * (n - len(k)) + k for k in tab_binaire]
    combinaisons_valide = []

    for combi in combinaisons:
        price_combi = 0
        net_combi = 0
        for i in range(n):
            if combi[i] == '1':
                price_combi += tab_import_csv[i]['price']
                net_combi += tab_import_csv[i]['net profit']

        if price_combi <= price_max:
            combinaisons_valide.append((combi, price_combi, net_combi))

    solution_optimale = combinaisons_valide[0][0]
    net_max = combinaisons_valide[0][2]

    for combi in combinaisons_valide:
        if combi[2] > net_max:
            net_max = combi[2]
            solution_optimale = combi[0]

    print(f'La solution optimale est {solution_optimale} avec un profit max {net_max}')
    liste_optimale = []

    for i in range(len(solution_optimale)):
        if solution_optimale[i] == '1':
            liste_optimale.append(tab_import_csv[i])

    print(f'solution optimale = {liste_optimale}')


tab_import_csv = import_csv('brute.csv')

start_time = datetime.now()
print(bruteForce(tab_import_csv, 500))
end_time = datetime.now()
print('time brutforce -> {}'.format(end_time - start_time))

start_time = datetime.now()
print(algo_sac_a_dos(tab_import_csv, 500))
end_time = datetime.now()
print('time brutforce -> {}'.format(end_time - start_time))