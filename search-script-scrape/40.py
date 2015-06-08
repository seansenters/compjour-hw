import json

In [227]: import requests

In [228]: data_url = "https://data.cityofchicago.org/resource/n379-5uzu.json"

In [229]: response = requests.get(data_url)

In [230]: text = response.text

In [231]: data = json.loads(text)

In [232]: len(data)
Out[232]: 83
