import csv

In [87]: import requests

In [88]: CSVURL = "http://www.fda.gov/downloads/ICECI/Inspections/UCM346093.csv"

In [89]: response = requests.get(CSVURL)

In [90]: f = open("UCM346093.csv", "w")

In [91]: f.write(response.text)

In [93]: f.close()

In [94]: data = csv.DictReader(open("UCM346093.csv"))

In [95]: rows = list(data)

In [97]: len(rows)
Out[97]: 23850
