import requests

import json

data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'

data = json.loads(requests.get(data_url).text)

books = data['results']['books']

x = 0

for a in books:
    if a['publisher'] == "Scribner":
        x += 1
        

print('A.', x)
('A.', 3)

counter = 0

for a in books:
    if "detective" in a['description'].lower():
        counter += 1
        

print('B.', counter)
('B.', 3)

max_val = 0

max_weeks = 'No weeks'

for a in books:
    if a['weeks_on_list']>max_val:
        max_val = a['weeks_on_list'] 
        max_weeks = a['title']
        

print('C.', max_weeks, "|", max_val)
('C.', u'THE GOLDFINCH', '|', 56)

max_val = 0

max_weeks = 'No weeks'

current_rank = 'rank'

for a in books:
    if a['rank_last_week']>max_val:
        max_val = a['rank_last_week']
        max_weeks = a['title']
        current_rank = a['rank']
        

print("D.", max_weeks, "|", current_rank, "|", max_val)
('D.', u'SOMEWHERE SAFE WITH SOMEBODY GOOD', '|', 16, '|', 14)

x = 0

for a in books:
    if a['rank_last_week'] == 0:
        x += 1
        

print("E.", x)
('E.', 6)

COME BACK TO F

def calc_rank_change(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]


books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]

x = max(books_ranked_last_week, key = calc_rank_change)

s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])

print('G.', s)
('G.', u'THE GOLDFINCH|11|2')

def calc_rank_drop(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]

books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]

x = min(books_ranked_last_week, key = calc_rank_drop)

s = "|".join([x['title'], str(x['rank']), str(calc_rank_drop(x))])

print('H.', s)
('H.', u'THE BOSTON GIRL|15|-3')

changes = [calc_rank_change(b) for b in books_ranked_last_week]

x = [v for v in changes if v > 0]

s = sum(x)

print('I.', s)
('I.', 4)

changes = [calc_rank_change(b) for b in books_ranked_last_week]

x = [v for v in changes if v < 0]

s = sum(x)

rint(x)
[-2, -1, -2, -2, -3, -2]

len(x)
Out[317]: 6

print('J.', len(x), "|", s)
('J.', 6, '|', -12)

 print('K.', max([len(b['title']) for b in books]))
('K.', 33)

x = 0

for b in books:
    x += b['title']
    
x = 0

for b in books:
    if b['title']:
        x += 1
        
print('L.', round((sum(len(b['title']) for b in books) / x)))
('L.', 16.0)
