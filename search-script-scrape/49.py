import json

In [148]: import requests

In [149]: data_url = 'http://congress.api.sunlightfoundation.com/bills?history.vetoed=true&sponsor_id=P000197&apikey=1b08f3ed3a9441939f82d87a6ba85a49'

In [150]: response = requests.get(data_url)

In [151]: text = response.text

In [152]: data = json.loads(text)

In [153]: print(data['count'])
0
