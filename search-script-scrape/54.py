import bs4

In [142]: import requests

In [143]: response = requests.get('http://www.fbi.gov/wanted/wcc/@@wanted-group-listing')

In [144]: soup = bs4.BeautifulSoup(response.text)

In [145]: link = soup.select("div.wanted-person-container-wrapper")

In [146]: len(link)
Out[146]: 36
