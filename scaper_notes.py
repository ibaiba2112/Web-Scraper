from bs4 import BeautifulSoup # Retrieving Beautiful Soup library
""" 
For ease of Writing, BeautifulSoup == bs4
"""

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

# print(soup.get_text()) #Gets all text
# print(soup.find_all('b'))



for link in soup.find_all('a'):
    print(link.get('href'))
# OR 
# for link in soup.find_all('a'):
#     print(link)