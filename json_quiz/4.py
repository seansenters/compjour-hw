In [144]: import requests

In [145]: import json

In [146]: data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"

In [147]: data = json.loads (requests.get(data_url).text)

In [148]: print ('A.', len(data['artists']))
('A.', 20)

In [149]: print ('B.', data['artists'][4]['name'])
('B.', u'Ciara')

In [150]: print ('C.', data['artists'][11]['followers']['total'])
('C.', 74258)

In [153]: print ('D.', data['artists'][0]['genres'])
('D.', [u'pop christmas', u'r&b', u'urban contemporary'])

In [156]: print ('E.', data['artists'][19]['images'][0]['url'])
('E.', u'https://i.scdn.co/image/7e8849593bcf16705c62128ed749de0e543c2e4e')
