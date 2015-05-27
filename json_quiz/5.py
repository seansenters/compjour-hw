In [157]: import requests

In [158]: import json

In [159]: data_url = "http://www.compjour.org/files/code/json-examples/single-tweet-librarycongress.json"

In [160]: data = json.loads(requests.get(data_url).text)

In [161]: print ('A.', data['created_at'])
('A.', u'Thu Apr 09 18:00:05 +0000 2015')

In [162]: print ('B.', data['user']['created_at'])
('B.', u'Fri Jun 29 14:23:25 +0000 2007')

In [163]: print ('C.', data['text'])
('C.', u'Passing by one vote, US Senate ratifies a treaty to purchase Alaska #OTD 1867. More: #ChronAm http://t.co/2RXNSMmOkf')

In [164]: print ('D.', data['user']['name'])
('D.', u'Library of Congress')

In [165]: print ('E.', data['id'])
('E.', 586227094285225984)

In [167]: print ('F.', data['entities']['user_mentions'])
('F.', [])

In [168]: hashtag_objs = data['entities']['hashtags']

In [169]: hashtag_texts = []

In [173]: for h in hashtag_objs:
     ...:     hashtag_texts.append(h['text'])
     ...:     
     ...:     
     ...:     
     ...:     

In [174]: print('G.', ','.join(hashtag_texts))
('G.', u'OTD,ChronAm')
