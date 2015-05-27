import requests

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

state_name = 'Alaska'

atts = {"CountrySubdivision":  state_name, 'NumberOfJobs':  1}

resp = requests.get(BASE_USAJOBS_URL, params = atts)

data = resp.json()

print("%s has %s job listings." % (state_name, data['TotalJobs']))

Alaska has 230 job listings.

import requests

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

state_name = 'Hawaii'

atts = {"CountrySubdivision":  state_name, 'NumberOfJobs':  1}

resp = requests.get(BASE_USAJOBS_URL, params = atts)

data = resp.json()

print("%s has %s job listings." % (state_name, data['TotalJobs']))

Hawaii has 181 job listings.

sum_states = 230+181

print("Together, they have %s job listings." %(sum_states))
Together, they have 411 job listings.
