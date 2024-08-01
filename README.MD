# Web Scaper/Crawler

Most of this is learning resources for myself, It's just a basic wbe scraper, the actual script is the web_scraper_test.txt, 
The description is found in the docstring

## Resources
* https://beautiful-soup-4.readthedocs.io/en/latest/
* https://pypi.org/project/beautifulsoup4/

## Learning 

### **html_doc**
<hr>

In the readthedocs page, The html file had a line I didn't understand, named "html_doc = """.

*Example.*

```html
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```
That html_doc line is actually a variable in python, it stores the html document in the variable so the scaper get pull the data out of it


### **BeautifulSoup Library**
<hr>
I need to download BeautifulSoup library to pull the data out of html and xtml, I also checked that you can downlaod some other parsing extensions but I will stick with the built in parser

*command line installation* 
```bash
python3 -m pip beautifulsoup4
```
running -m ensures running the module directly from the command line and runs the moduele as if it was a script
*Result*
```bash
macbookpro@Macbooks-MacBook-Pro Web Scraper % python3 -m pip install beautifulsoup4
Collecting beautifulsoup4
  Obtaining dependency information for beautifulsoup4 from https://files.pythonhosted.org/packages/b1/fe/e8c672695b37eecc5cbf43e1d0638d88d66ba3a44c4d321c796f4e59167f/beautifulsoup4-4.12.3-py3-none-any.whl.metadata
  Downloading beautifulsoup4-4.12.3-py3-none-any.whl.metadata (3.8 kB)
Collecting soupsieve>1.2 (from beautifulsoup4)
  Obtaining dependency information for soupsieve>1.2 from https://files.pythonhosted.org/packages/4c/f3/038b302fdfbe3be7da016777069f26ceefe11a681055ea1f7817546508e3/soupsieve-2.5-py3-none-any.whl.metadata
  Downloading soupsieve-2.5-py3-none-any.whl.metadata (4.7 kB)
Downloading beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 147.9/147.9 kB 1.8 MB/s eta 0:00:00
Downloading soupsieve-2.5-py3-none-any.whl (36 kB)
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.12.3 soupsieve-2.5
```
Check your pip and python is up to date
```bash
python3 --version
```
```bash
pip3 --version
```
<hr>

### **Python Script**
It's quite simple, The library does most of the work
```python
from bs4 import BeautifulSoup # Retrieving Beautiful Soup library

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
"""
Soup = BeautifulSoup ==> This creates a BeautifulSoup object called "Soup", this uses the bs4 library, which is used for parsing data out of html and xml docs
"html.parser" ==> is the parser the library is using, html.parser is the default, built in python parser. you can specifiy  otherwise if you want something different

Now the soup has put the html doc into a nested data data steructure, which is easier to navigate and pull things from
"""
# print(soup.prettify())
"""
This prints the nested data structure, html_doc, 
soup.prettify ==> literally just makes the data more readable and in a nicer format
"""
```

This is the basics of it.
Here are some more examples
```python
print(soup.get_text) # This retrieves all text
```

```python
print(soup.find_all('b')) # This retrieves all lines with 'b', This might look messy as it will be on one line, so best to use a for loop
```
```python
for link in soup.find_all('a'):
    print(link)

    """
    would print like this
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    """
```
if you want to be really fancy and just show the urls, no tags or elements, you can use .get
```python
for link in soup.find_all('a'):
    print(link.get('href'))

    """ 
    http://example.com/elsie
    http://example.com/lacie
    http://example.com/tillie
    """
```

This is mostly the scraping done now, Now we will need to use requests to make http requests to page to actually launch the web scraper

### **HTTP Requests**
<hr>
Now we need to use the requests library in python to handle http requested to pages and stuff

*Commmand to install Requests*
```bash
python3 -m pip install requests
```