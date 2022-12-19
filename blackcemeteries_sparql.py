import requests
import json


#extract data from Wikidata SPARQL query
url = "https://query.wikidata.org/sparql"

sparql = """

#African American Cemeteries
SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q39614.
  ?item wdt:P17 wd:Q30.
  ?item wdt:P5008 wd:Q15304953.
 
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
  'Accept' : 'application/json',
  'User-Agent': 'Mozzilla-Firefox'
}

r = requests.get(url, params=params, headers=headers)

data = json.loads(r.text)


# "results" : {
#     "bindings" : [ {
#       "item" : {

for results in data['results']['bindings']:

  # print(json.dumps(results,indent=2))
  if 'itemLabel' in results:
      print(results['itemLabel']['value'])




