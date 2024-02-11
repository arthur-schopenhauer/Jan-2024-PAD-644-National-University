from serpapi import GoogleSearch as Google_Scholar
import json
import os
import re

params = {
  "api_key": "PASS_KEY",
  "engine": "google_scholar",
  "q": "temp",
  "hl": "en",
  "num": "20",
  "start": "0"
}

search_keywords = [
    "Residential Evictions",
    "San Diego County",
    "COVID-19",
    "Emergency Rent Assistance Program",
    "ERAP",
    "Human Service Organizations",
    "HSO",
    "Case Management Strategies",
    "HSO OR HSO",
    "Residential Evictions AND San Diego County",
    "Residential Evictions NOT San Diego County",
    "Residential Evictions OR San Diego County",
    "COVID-19 AND Emergency Rent Assistance Program",
    "COVID-19 NOT Emergency Rent Assistance Program",
    "COVID-19 OR Emergency Rent Assistance Program",
    "ERAP AND Human Service Organizations",
    "ERAP NOT Human Service Organizations",
    "ERAP OR Human Service Organizations",
    "HSO AND Case Management Strategies",
    "HSO NOT Case Management Strategies",
    "HSO OR Case Management Strategies",
    "Residential Evictions AND San Diego County",
    "Residential Evictions NOT San Diego County",
    "Residential Evictions OR San Diego County",
    "COVID-19 AND Emergency Rent Assistance Program",
    "COVID-19 NOT Emergency Rent Assistance Program",
    "COVID-19 OR Emergency Rent Assistance Program",
    "ERAP AND Human Service Organizations",
    "ERAP NOT Human Service Organizations",
    "ERAP OR Human Service Organizations",
    "HSO AND Case Management Strategies",
    "HSO NOT Case Management Strategies",
    "HSO OR Case Management Strategies",
    "San Diego County NOT Residential Evictions",
    "San Diego County OR Residential Evictions",
    "Emergency Rent Assistance Program AND COVID-19",
    "Emergency Rent Assistance Program NOT COVID-19",
    "Emergency Rent Assistance Program OR COVID-19",
    "Human Service Organizations AND ERAP",
    "Human Service Organizations NOT ERAP",
    "Human Service Organizations OR ERAP",
    "Case Management Strategies AND HSO",
    "Case Management Strategies NOT HSO",
    "Case Management Strategies OR HSO"

]

def filter_dict(data: dict, extract):
    try:
        if isinstance(extract, list):
            while extract:
                if result := filter_dict(data, extract.pop(0)):
                    return result
        shadow_data = data.copy()
        for key in extract.split('.'):
            if str(key).isnumeric():
                key = int(key)
            shadow_data = shadow_data[key]
        return shadow_data
    except (IndexError, KeyError, AttributeError, TypeError):
        return None

def sources(counter, data, position):
    try:
        for term in search_keywords:
        	import re
        	position = str(position)
        	message = term + "\n" +"""(
        	source number: {0},
        	title: {1},
        	url: {2},
        	short extract: {3},
        	authors, and year: {4},
        	popularity: {5},
        	),
        	"""
        	data = data["organic_results"]
        	title = filter_dict(data, str(position)+'.title')
        	url = filter_dict(data, str(position)+'.link')
        	snip = filter_dict(data, str(position)+'.snippet')
        	summ = re.split("-",filter_dict(data, str(position)+'.publication_info.summary'))
        	popular = filter_dict(data, str(position)+'.inline_links.cited_by.total')
        	file.write( message.format(str(int(position)+counter), title, url, snip, summ, popular))
    except:
        pass

# Use the Google Scholar function to get search results
# search = Google_Scholar(params)
for term in search_keywords:
    params["q"] = term
    search = Google_Scholar(params)
    results = search.get_dict()
    for record in range(20):
        file = open("SEARCH_RESULTS.txt", "a")
        sources(0, results, record)
        file.close()

