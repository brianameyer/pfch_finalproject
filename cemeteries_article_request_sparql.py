import requests
import json

url = "https://query.wikidata.org/sparql"

sparql = """

	SELECT ?item ?itemLabel ?article
	WHERE 
	{
	  ?item wdt:P31 wd:Q39614. 
	  ?item wdt:P17 wd:Q30.

	  OPTIONAL {
	    ?article schema:about ?item .
	    ?article schema:inLanguage "en" .
	    FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/")
	  }  
	  
	  
	  
	  
	  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # Helps get the label in your language, if not, then en language
	}

	limit 5000


"""

# set some params and headers to tell wikidata who is makeing the request
params = {
	'query' : sparql
}

headers = {
	'Accept' : 'application/json',
	'User-Agent': 'USER PFCH - Test Script '
}

r = requests.get(url, params=params, headers=headers)

data = json.loads(r.text)


 # this is the format it comes back as
 # "results" : {
 #    "bindings" : [ {
 #      "item" : {

for result in data['results']['bindings']:
	

	wikidata_uri = result['item']['value']
	label = result['itemLabel']['value']

	article_url = None

	if 'article' in result:
		
		article_url = result['article']['value']


	if article_url != None:

		print(wikidata_uri,label,article_url)

		title = article_url.split('/wiki/')[-1] 

		print(title)

		article_text_api_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&titles={title}&prop=extracts&exintro&explaintext"

		r = requests.get(article_text_api_url, headers=headers)

		article_response = r.json()

		print(article_response)

		article_text = article_response['query']['pages']

	
		first_key = list(article_text.keys())[0]

		article_text = article_text[first_key]['extract']

		print(article_text)

	look_for = ['Black','African','african','black','enslaved','slavery']

	for word in look_for:

		if word in article_text:

			print("---------------Article text references---------------", word)

