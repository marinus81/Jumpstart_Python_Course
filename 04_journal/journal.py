import os

def load(journal_name):
    #todo populate from file
    return []

def save(journal_name, journal_data):
    file_name = get_filename(journal_name)
    with open(file_name, 'w') in fout:


def get_filename(journal_name):
    file_name = os.path.abspath(os.path.join('.', 'journals', journal_name + '.jrn'))
    return file_name


def add_entry(data, text):
    data.append(text)
    return None