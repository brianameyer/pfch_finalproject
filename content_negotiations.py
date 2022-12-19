import requests

url = "https://query.wikidata.org/sparql"

sparql = """

#African American Cemeteries
SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q39614. # Must be of a African-American cemetery
  ?item wdt:P17 wd:Q30.
 
 OPTIONAL {
    ?article schema:about ?item .
    ?article schema:inLanguage "en" .
    FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/")
  } 
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # Helps get the label in your language, if not, then en language
}

"""

params = {
	
	'query' : sparql
}

headers = {
  'Accept' : 'application/json'
}

r = requests.get(url, params=params, headers=headers)

print(r.text)