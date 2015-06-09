import bs4

import requests

data_url = "http://www.legis.ga.gov/Legislation/en-US/display/20152016/HB/106"

response = requests.get(data_url)

soup = bs4.BeautifulSoup(response.text)

link = soup.select("div.item")[3]

print(link.text)
A BILL to be entitled an Act to amend Title 32 of the Official Code of Georgia Annotated, relating to highways, bridges, and ferries, so as to revise what constitutes part of the state highway system; to provide for the appropriation of funds to the Department of Transportation; to amend Title 40 of the Official Code of Georgia Annotated, relating to motor vehicles and traffic, so as to provide for submission of electronic accident reports by law enforcement agencies; to repeal conflicting laws; and for other purposes. 
