import requests

from bs4 import BeautifulSoup

def extract_headlines(url):

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        headlines =soup.find_all('h2')

        for headline in headlines:

            print(headline.text.strip())

website_url ="https://www.wikipedia.org/"

extract_headlines(website_url)     