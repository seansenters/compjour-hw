import requests

import json

data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'

data = json.loads(requests.get(data_url).text)

books = data['results']['books']

