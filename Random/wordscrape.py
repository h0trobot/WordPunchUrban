from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
import io
import ssl
import selenium.webdriver as webdriver
from random import randint

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z'
]

numbers = range(1, 232)
word_links = []
'''for number in numbers:
    url = 'https://www.macmillandictionary.com/open-dictionary/index-chronological-order_page-' + str(number) + '.htm'
    with webdriver.Firefox() as browser:
        browser.get(url)
        words = browser.find_elements_by_xpath("//a[@class='red-hover']")
        print(words)
        href = words.get_attribute("href")
        word_links.append(href)
        print(words)
for link in word_links:
    with webdriver.PhantomJS() as browser:
        browser.get(link)
        base = browser.find_elements_by_xpath("//h1//span[@class='BASE']")
        definition = browser.find_elements_by_xpath("//h1//span[@class='DEFINITION']")
'''
word_definitions = {}
words_list = []
for number in numbers:
    headers = {
        "User-Agent": "Mozilla/84.0.2"}
    url = 'https://www.macmillandictionary.com/open-dictionary/index-chronological-order_page-' + str(number) + '.htm'
    gcontext = ssl.SSLContext()

    with urlopen((Request(url=url, headers=headers)), context=gcontext) as client:
        page_html = client.read()
    page_soup = soup(page_html, "html.parser")

    word_panel = page_soup.find("div", {"class": "gray-box"})
    words_list = word_panel.findAll("li", {"class": "col-xs-12 col-sm-6"})
    print(words_list)

for word in words_list:
    word_link = word.a["href"]
    with urlopen(word_link) as word_client:
        word_html = word_client.read()
    word_soup = soup(word_html, "html.parser")

    def_panel = word_soup.findAll("div", {"class", "col-xs-12 col-sm-8 col-md-content-with-right left-content"})
    top_definition = def_panel[0]
    term = top_definition.findAll("span", {"class", "BASE"})
    meaning = top_definition.findAll("span", {"class", "DEFINITION"})

    with io.open('macmillian_scrape.txt', 'a', encoding='utf-8') as f:
        f.write("\'" + term[0].text + "\'" + ':\n' + "\'" + meaning[0].text + "\'," +'\n\n')
    word_definitions[term[0].text] = meaning[0].text
    print(term[0].text + ':\n' + meaning[0].text + '\n')

'''
for letter in alphabet:
    headers = {
        "User-Agent": "Mozilla/84.0.2"}
    url = 'https://www.urbandictionary.com/popular.php?character=' + letter

    with urlopen((Request(url=url, headers=headers))) as client:
        page_html = client.read()
    page_soup = soup(page_html, "html.parser")

    word_panel = page_soup.find("div", {"class": "panel collection-panel"})
    words_list = word_panel.findAll("li", {"class": "word"})
    word_definitions = {}

    for word in words_list:
        word_link = word.a["href"]
        with urlopen('https://www.urbandictionary.com' + word_link) as word_client:
            word_html = word_client.read()
        word_soup = soup(word_html, "html.parser")

        def_panel = word_soup.findAll("div", {"class", "def-panel"})
        top_definition = def_panel[0]
        term = top_definition.findAll("a", {"class", "word"})
        meaning = top_definition.findAll("div", {"class", "meaning"})
        with io.open('lexic glossary.txt', 'a', encoding='utf-8') as f:
            f.write("\'" + term[0].text + "\'" + ':\n' + "\'" + meaning[0].text + "\'" +'\n\n')
        word_definitions[term[0].text] = meaning[0].text
        print(term[0].text + ':\n' + meaning[0].text + '\n')
'''













