import bs4

import requests

data_url = "http://www.dol.gov/whd/minwage/america.htm#Consolidated"

response = requests.get(data_url)

soup = bs4.BeautifulSoup(response.text)

link = soup.select("table")[10]

print(link.text)

District of Columbia Minimum Wage Rates

 DISTRICT
            OF COLUMBIA
Basic Minimum Rate(per
            hour)
Premium
            Pay
                        After Designated Hours 2


Daily
Weekly


 
$9.50
 
40
