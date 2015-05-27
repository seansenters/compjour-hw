import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
countries = 'China', 'South Africa', 'Tajikistan'
for country in countries:
   atts = {"Country": country, 'NumberOfJobs': 1}
   resp = requests.get(BASE_USAJOBS_URL, params = atts)
   data = resp.json()
   print("%s has %s job listings." % (country, data['TotalJobs']))

sum_countries = 13+4+7
print("Together, they have %s job listings." %(sum_countries))

China has 13 job listings.
South Africa has 4 job listings.
Tajikistan has 7 job listings.
Together, they have 24 job listings.
