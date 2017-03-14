import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'filename, line_num, text')


def main():
    print_header()
    folder = get_folder()
    if not folder:
        print('Sorry this folder name is invalid')
        return

    text = get_text()
    if not text:
        print('Sorry this folder name is invalid')
        return

    matches = search_folders(folder, text)

    for m in search_folders(folder, text):
        print('--------------MATCH---------------')
        print('file: '+ m.filename)
        print('line: {}'.format(m.line_num))
        print('text: '+m.text.strip())
        print()


def print_header():
    print('---------------------------------------------')
    print('           FILE SEARCHER APP')
    print('---------------------------------------------')


def get_folder():
    folder = input('Which folder to search in: ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_text():
    text = input('What text to search for: ')
    return text


def search_file(filename, text):
    #matches = []

    with open(filename, 'r', encoding='utf-8') as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(text) >= 0:
                m = SearchResult(line_num=line_num, text=line, filename=filename)
                #matches.append(m)
                yield m

    #return matches


def search_folders(folder, text):
    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # matches = search_folders(full_item, text)
            yield from search_folders(full_item, text)

            #for m in matches:
            #    yield m
        else:
#            matches = search_file(full_item, text)
             yield from search_file(full_item, text)
#            for m in matches:
#                yield m
        #all_matches.extend(matches)

    #return all_matches


if __name__ == '__main__':
    main()
