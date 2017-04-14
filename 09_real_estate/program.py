import csv
import os
from purchase import Purchase


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #    print(row)
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            purchases.append(Purchase.from_dict(row))

        print(purchases[0].__dict__)
        return purchases


def query_data(data: list):
    data.sort(key=lambda p: p.price)
    # highest price
    highest = data[-1]
    print("Highst price was {} for a house with {} beds and {} baths".format(highest.price, highest.beds, highest.baths))

    # lowest price
    lowest = data[0]
    print("Lowest price was {} for a house with {} beds and {} baths".format(lowest.price, lowest.beds, lowest.baths))

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)

    pass


def print_header():
    print('----------------------------------------------')
    print('         REAL ESTATE ANALYSER APP ')
    print('----------------------------------------------')
    print('')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', "transactions.csv")


if __name__ == '__main__':
    main()
