import os


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

    pass


def query_data(data):
    pass


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)
    
    pass

def print_header:
    print('----------------------------------------------')
    print('         REAL ESTATE ANALYSER APP ')
    print('----------------------------------------------')
    print('')

def get_data_file:
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', transactions.csv)


if __name__ == '__main__':
    main()