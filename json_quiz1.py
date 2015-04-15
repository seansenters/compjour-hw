import requests

import json

data_url = "http://www.compjour.org/files/code/json-examples/analyticsgov-realtime.json"

response = requests.get (data_url)

text = response.text

data = json.loads (text)

print ('A.', data['name']
)
('A.', u'realtime')

print ('B.', data['taken_at'])
('B.', u'2015-04-13T03:20:02.401Z')

print('C.', data['meta']['name'])
('C.', u'Active Users Right Now')

print('D.', data['data'][0]['active_visitors']
)
('D.', u'78000')

print('E.', ', '.join(data.keys()))
('E.', u'name, totals, meta, taken_at, query, data')

