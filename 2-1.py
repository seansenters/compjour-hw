import json

In [51]: import os

In [52]: import requests

In [53]: BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

In [54]: CODES_URL = "http://stash.compjour.org/data/usajobs/CountryCode.json"

In [55]: cdata = requests.get(CODES_URL).json()

In [56]: mylist = []

In [57]: for d in cdata['CountryCodes']:
    ...:     if d['Code'] != 'US' and d['Value'] != 'Undefined':
    ...:         cname = d['Value']
    ...:         print("Getting:", cname)
    ...:         atts = {'Country': cname, 'NumberOfJobs': 1}
    ...:         resp = requests.get(BASE_USAJOBS_URL, params = atts)
    ...:         data = resp.json()
    ...:         jobcount = int(data['TotalJobs'])
    ...:         mylist.append([cname, jobcount])
    ...: os.makedirs("data-hold", exist_ok = True)
    ...: f = open("data-hold/intl-jobcount.json", 'w')
    ...: f.write(json.dumps(mylist, indent = 2))
    ...: f.close()
