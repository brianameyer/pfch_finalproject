# pfch_finalproject
PFCH Final Project

This repository was completed as the final assignment for INFO-664-Programming For Cultural Heritage at the Pratt Institute during the Fall 2022 semester and focused on uncovering forgotten histories of African American cemeteries in the United States.

Initially, I set out to determine a way to explore and analyze Black Cemeteries across the United States. I aimed to capture the perpetual neglect of these spaces by drawing attention to the lack of data collected on those buried within the cemeteries and the cemeteries themselves — emphasizing the blatant racism and inequality haunting Black Americans even in death.

In conducting SPARQL Queries in Wikidata and Python, I’ve explored, analyzed, and identified Black Cemeteries across the United States with the intent of finding a way to capture the perpetual neglect of these spaces by drawing attention to the lack of data collected on those buried within the cemeteries and the cemeteries themselves. To accomplish this, I identified African American Cemeteries within the United States on Wikidata, through a SPARQL query, by identifying the specific items and instances to target my search. I also added an optional article search to initiate text return to determine key terms that identify each cemetery as a burial ground for African Americans. Once I generated the search, I used the URL, and User Agent found in the developer tools and my Wikidata SPARQL query to write a SPARQL query in Python. 

After inputting the Wikidata query, I then defined parameters and headers for the request to generate JSON and begin analyzing data. For the next step, I requested plain text within the search return for cemeteries within the United States by identifying the dictionary and printing the article text. The result displayed defined information, including item, type, Uri, and value, and noted which returns included the terms “African,” “african,” “Black”, “black”, “enslaved”, “slavery”, “Freedpeople”, “freedpeople”, “Freedperson” and “freedperson.” In writing a SPARQL python request, I successfully identified a list of African American cemeteries and distinguished the terms used to categorize the cemeteries as African American burial grounds within the United States, as this was unidentifiable solely based on extracting the list of cemeteries. 
