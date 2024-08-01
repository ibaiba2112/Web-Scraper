import requests
from bs4 import BeautifulSoup
import re

def web_scraper(url, file_output):
    '''
    Web Scraping Function

    Parameters:
    url (str): user gives valid url when prompted, url will be used to fetch and parse the webpage
    file_output (str): user give this file a name, this file will contain the extarcted data

    Returns:
    Returns extracted data from webpage and writes to a txt file, this function looks for links, preferably emails
    '''
    response = requests.get(url)
    if response.status_code == 200:
        html_doc = response.text

        soup = BeautifulSoup(html_doc, "html.parser")
        # print(soup.prettify()) # Uncomment if you want to print the whole html document

        email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')



        with open(file_output, 'a') as fout:
            for link in soup.find_all('a'): # "href=True" ensures only <a> elements with hrefs get extracted
                href = link.get('href')
                
                if "mailto:" in href and href.endswith(".ie"):
                    fout.write(href + '\n')

            for script in soup.find_all('script'):
                script_content = script.string
                if script_content:
                    # Search for email addresses within the script content
                    emails = email_regex.findall(script_content)
                    for email in emails:
                        fout.write(email + '\n')
    else:
        print("Failed to retrieve webpage!", response.status_code)

# URL and Output File name prompt
url = input("Give a URL: ")
file_output = input("Name your file you want the data sent to, (must end with .txt): ")
web_scraper(url, file_output)