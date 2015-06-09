import requests
from operator import itemgetter
url = "https://data.consumerfinance.gov/api/views/c8k9-ryca/rows.json?accessType=DOWNLOAD"
data = requests.get(url).json()
cols = data['meta']['view']['columns']
d_pos = next((i for i, c in enumerate(cols) if c['name'] == 'Date received'), -1)
c_pos = next((i for i, c in enumerate(cols) if c['name'] == 'Company'), -1)
row = max(data['data'], key = itemgetter(d_pos))
print(row[c_pos])
