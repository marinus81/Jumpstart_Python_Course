import os

def load(journal_name):
    data= []
    file_name = get_filename(journal_name)

    if os.path.exists(file_name):
        with open(file_name) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(journal_name, journal_data):
    file_name = get_filename(journal_name)
    with open(file_name, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_filename(journal_name):
    file_name = os.path.abspath(os.path.join('.', 'journals', journal_name + '.jrn'))
    return file_name


def add_entry(data, text):
    data.append(text)
    return None