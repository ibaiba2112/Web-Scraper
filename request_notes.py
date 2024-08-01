import requests

 
url = "https://en.wikipedia.org/wiki/Paul_Simonon" # url i want to retrieve data from 

response = requests.get(url) # Using the library, response will send http get request to url

if response.status_code == 200: # if 200 OK
    html_doc = response.text # get doc content from response
else:
    print("Failed to retrieve webpage!")
