"""
This is the journal module. It handles the internal data structure as well as file save and load
"""

import os

def load(journal_name):
    """
    Load a journal file and populate a list element with its data

    :param journal_name: The filename for the journal to load. Expected to be located in the journals subdirectory.
    :return: a list with all journal entries
    """
    data= []
    file_name = get_filename(journal_name)

    if os.path.exists(file_name):
        with open(file_name) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(journal_name, journal_data):
    """
    Save Data to a file

    :param journal_name: filename of the file where data will be saved
    :param journal_data: data of the journal to be saved in a file
    :return: None
    """
    file_name = get_filename(journal_name)
    with open(file_name, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_filename(journal_name):
    """
    Get the absolute filename path for file journal_name in 'journals' subdirectory

    :param journal_name: filename
    :return:
    """
    file_name = os.path.abspath(os.path.join('.', 'journals', journal_name + '.jrn'))
    return file_name


def add_entry(data, text):
    """
    Add a text entry to the list

    :param data: list of all entries
    :param text: text to add
    :return: None
    """
    data.append(text)
    return None