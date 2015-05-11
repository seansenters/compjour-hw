import json

In [72]: import os

In [73]: import requests

In [74]: BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

In [75]: CODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"

In [76]: cdata = requests.get(CODES_URL).json()

In [77]: mylist = []

In [78]: statelist = []

In [79]: for c in cdata:
    ...:     statelist.append(c)
    ...:     

In [80]: for c in statelist:
    ...:     atts = {'CountrySubdivision': c, 'NumberOfJobs': 1}
    ...:     resp = requests.get(BASE_USAJOBS_URL, params = atts)
    ...:     data = resp.json()
    ...:     jobcount = int(data['TotalJobs'])
    ...:     mylist.append([c, jobcount])
    ...:     

In [84]: os.makedirs("data-hold")

In [85]: f = open("data-hold/domestic-jobcount", "w")

In [86]: f.write(json.dumps(mylist, indent = 2))

In [87]: f.close()
