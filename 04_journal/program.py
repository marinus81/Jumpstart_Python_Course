import journal


def print_header():
    print('--------------------------------------------')
    print('         Journal Diary')
    print('--------------------------------------------')


def event_loop():
    print('What do you want to do?')
    cmd = None

    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x':
        cmd = input('You can [L]ist or [A]dd enttries or E[x]it:')

        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry we do not understand '{}'".format(cmd))

    journal.save(journal_name, journal_data)
    print("Done. Goodbye!")


def list_entries(data):
    print("Your entries:")
    for (index, entry) in enumerate(reversed(data)):
        print('Entry {}:'.format(index))
        print(entry)


def add_entry(data):
    text = input("Type your entry:")
    journal.add_entry(data,text)



def main():
    print_header()
    event_loop()


main()
