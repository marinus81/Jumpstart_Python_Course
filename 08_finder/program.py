import os


def main():
    print_header()
    folder=get_folder()
    if not folder:
        print('Sorry this folder name is invalid')
        return

    text=get_text()
    if not text:
        print('Sorry this folder name is invalid')
        return

    matches = search_folders(folder,text)

    for m in matches:
        print(m)


def print_header():
    print ('---------------------------------------------')
    print ('           FILE SEARCHER APP')
    print ('---------------------------------------------')

def get_folder():
    folder=input('Which folder to search in: ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_text():
    text=input('What text to search for: ')
    return text


def search_file(filename, text):
    matches = []

    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            if line.lower().find(text) >= 0:
                matches.append(line)

    return matches


def search_folders(folder, text):
    all_matches = []
    items=os.listdir(folder)

    for item in items:
        full_item=os.path.join(folder,item)
        if os.path.isdir(full_item):
            continue

        matches = search_file(full_item, text)
        all_matches.extend(matches)


    return all_matches

if __name__ == '__main__':
    main()
