import requests
import collections

MovieResult=collections.namedtuple('MovieResult','Title,Year,imdbID,Type,Poster')

class MovieClient():
    def __init__(self, search_text):
        if not search_text or not search_text.strip():
            raise ValueError(search_text)
        self.search_text=search_text


    def perform_search(self):

        url="http://www.omdbapi.com/?s={}".format(self.search_text)

        data=requests.get(url)
        results=data.json()['Search']

        movies = [MovieResult(**m) for m in results]
        movies.sort(key=lambda m: m.Year, reverse=True)

        return movies