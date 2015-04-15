In [123]: import requests

In [124]: import json

In [125]: data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"

In [126]: response = requests.get(data_url)

In [127]: text = response.text

In [128]: data = json.loads(text)

In [130]: result_obj = data['results'][0]

In [131]: print ('A.', result_obj['formatted_address'])
('A.', u'Stanford University, Main Quad, 450 Serra Mall McClatchy Hall, Stanford, CA 94305, USA')

In [132]: print ('B.', data['status'])
('B.', u'OK')

In [133]: print ('C.', result_obj['geometry']['location_type'])
('C.', u'ROOFTOP')

In [134]: print ('D.', result_obj['geometry']['location']['lat'])
('D.', 37.4283125)

In [138]: print ('E.', result_obj['geometry']['viewport']['southwest']['lng'])
('E.', -122.1708429802915)

In [143]: print ('F.', result_obj['address_components'][0]['long_name'], result_obj['address_components'][1]['long_name'])
('F.', u'McClatchy Hall', u'Stanford University')
