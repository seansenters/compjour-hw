import requests

import json

import os

data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'

tempfilename = "/tmp/congresslist.json"

if os.path.exists(tempfilename):
    tfile = open (tempfilename, "r")
    j = tfile.read()
else:
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)
    

tfile.close()

accounts = json.loads(j)

x = len(accounts) 

print('A.', x)
('A.', 571)

x = 0

for a in accounts:
    if a['followers_count'] > 10000:
        x += 1
        

print ("B.", x)
('B.', 231)

for a in accounts:
    if a['verified']:
        x += 1
        

print("C.", x)
('C.', 543)

counts = []

for a in accounts:
    counts.append(a['followers_count'])
    

maxval = sorted(counts, reverse = True)[0]

print ("D.", maxval)
('D.', 1955200)

counts = []

for a in accounts:
    counts.append(a['statuses_count'])
    

maxval = sorted(counts, reverse = True)[0]

print("E.", maxval)
('E.', 47169)

rom operator import itemgetter

y = sorted(accounts, key = itemgetter('followers_count'), reverse = True)

x = y[0]

print("F.", x['screen_name'], 'has', x['followers_count'], 'followers')
('F.', u'SenJohnMcCain', 'has', 1955200, 'followers')

COME BACK TO G

totes = 0

for a in accounts:
    totes += a['followers_count']
    

print ('H.', round(totes / len(accounts)))
('H.', 28909.0)

counts = []

for a in accounts:
    counts.append(a['followers_count'])
    

midval = sorted(counts, reverse = True)[285]

print("I.", midval)
('I.', 8385)
