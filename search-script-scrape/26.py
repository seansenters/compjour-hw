import bs4

import requests

data_url = "http://dq.cde.ca.gov/dataquest/cohortrates/GradRates.aspx?cds=43000000000000&TheYear=2013-14&Agg=O&Topic=Dropouts&RC=County&SubGroup=Ethnic/Racial"

response = requests.get(data_url)

soup = bs4.BeautifulSoup(response.text)

link = soup.select("span")[5]

print(link.text)
16,888

link = soup.select("span")[7]

print(link.text)
114

link = soup.select("span")[6]

print(link.text)
2,248
