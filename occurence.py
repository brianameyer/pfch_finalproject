# import requests
# import json
from collections import Counter

#extract data from Wikidata SPARQL query

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

# define who is making the request with parameters
params = {
	'query' : sparql
}

headers = {
'Accept' : 'application/json',
'User-Agent': 'USER PFCH - Test Script '
}

r = requests.get(url, params=params, headers=headers)

data = json.loads(r.text)


 #format below is how JSON result should look
 # "results" : {
 #    "bindings" : [ {
 #      "item" : {

article_counter = {'hasWord':0, 'doesNotHaveWord':0}
word_counter = {}


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

    #plain text keyword search

    article_text_api_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&titles={title}&prop=extracts&exintro&explaintext"

    r = requests.get(article_text_api_url, headers=headers)

    article_response = r.json()

    print(article_response)

    article_text = article_response['query']['pages']

	#identify dictionary key

    first_key = list(article_text.keys())[0]

    article_text = article_text[first_key]['extract']

    print(article_text)

    #Determine word occurance

    look_for = ["Black", "African", "african", "black", "enslaved", "Enslaved", "Slavery", "slavery","slave","Slave" "Free", "free", "Freed", "freed", "freedpeople", "Freepeaople", "Freedperson", "freedperson", "person of color", "African American", "african american","emancipation", "Emancipation", "Civil","civil", "Civil War", "civil war" ]

    found_a_word = False
    for word in look_for:

      if word in article_text:

        found_a_word = True
        if word not in word_counter:
          word_counter[word] = 0

        word_counter[word] = word_counter[word] + 1


    if found_a_word == True:
      article_counter['hasWord'] = article_counter['hasWord'] + 1
    else:
      article_counter['doesNotHaveWord'] = article_counter['doesNotHaveWord'] + 1



    print(word_counter)

    print(article_counter) 

