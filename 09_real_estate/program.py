import csv
import os
import statistics

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
    print("Highst price was ${:,} for a house with {} beds and {} baths".format(highest.price, highest.beds, highest.baths))

    # lowest price
    lowest = data[0]
    print("Lowest price was ${:,} for a house with {} beds and {} baths".format(lowest.price, lowest.beds, lowest.baths))

    #average price
    avg_price = statistics.mean([p.price for p in data])
    print("Average sell price was ${:,}".format(int(avg_price)))


    #average two bedrom price
    twobeds = [p for p in data if p.beds==2]
    avg_2bed_price=int(statistics.mean([p.price for p in twobeds]))
    avg_2bed_baths=round(statistics.mean([p.baths for p in twobeds]),1)
    avg_2bed_sqft=round(statistics.mean([p.sq__ft for p in twobeds]),1)
    print("Average 2 bed price: ${:,}, baths={}, avg sqft={}".format(avg_2bed_price,avg_2bed_baths,avg_2bed_sqft))

    twobeds_gen = (p for p in data if p.beds==2)
    prices=[p.price for p in twobeds_gen]
    print(prices)
    avg_2bed_price = int(statistics.mean(prices))
   # avg_2bed_baths = round(statistics.mean([p.baths for p in twobeds_gen]), 1)
   # avg_2bed_sqft = round(statistics.mean([p.sq__ft for p in twobeds_gen]), 1)
    print("Average 2 bed price: ${:,}, baths={}, avg sqft={}".format(avg_2bed_price, avg_2bed_baths, avg_2bed_sqft))


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
