import requests
import json
from tqdm import tqdm


class CountryIterator:

    def __init__(self, file_name, start):
        self.file_name = file_name
        self.start = start - 2

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file_name, encoding='utf-8') as f:
            countries_info = json.load(f)
        end = (len(countries_info))
        self.start += 1
        if self.start == end:
            raise StopIteration
        url = "https://en.wikipedia.org/w/api.php"
        searchpage = countries_info[self.start]['name']['common']
        params = {
            "action": "opensearch",
            "format": "json",
            "list": "search",
            "search": searchpage
        }
        response = requests.get(url=url, params=params)
        data = response.json()[1][0] + ' - ' + response.json()[3][0] + '\n'
        return data

    def __len__(self):
        with open(self.file_name, encoding='utf-8') as f:
            countries_info = json.load(f)
        lenght = (len(countries_info))
        return lenght


with open('result.txt', 'w', encoding='utf8') as res:
    with tqdm(total=CountryIterator('countries.json', 1).__len__()) as pbar:
        for line in CountryIterator('countries.json', 1):
            res.write(line)
            res.tell()
            pbar.update(1)
