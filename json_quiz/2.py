import requests

import json

data_url = "http://www.compjour.org/files/code/json-examples/graph.facebook-whitehouse.json"

response = requests.get(data_url)

text = response.text

data = json.loads(text)

print ('A.', data['checkins'])
('A.', 1474208)

print ('B.', data['likes'])
('B.', 3405748)

print ('C.', data['location']['longitude'])
('C.', -77.035704501759)

print ('D.', data['category_list'][1]['name'])
('D.', u'Government Organization')
