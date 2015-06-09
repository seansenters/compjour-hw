import bs4
import requests
data_url = "http://www.nyclu.org/content/stop-and-frisk-data"
response = requests.get(data_url)
soup = bs4.BeautifulSoup(response.text)
link = soup.select("li")[210]
print(link.text)

In 2014, New Yorkers were stopped by the police 46,235 times.
38,051 were totally innocent (82 percent).
24,777 were black (55 percent).
12,662 were Latino (29 percent).
5,536 were white (12 percent).
