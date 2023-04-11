#!/usr/bin/env python
from bs4 import BeautifulSoup
import time
import urllib.request


class WebsiteScraper:
    # Initialize necessary variables.
    def __init__(self, url):
        self.url = url
    
    # Scrape links from the web-page.
    def link_scraper(self,):
        data = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(data, 'html.parser')
        print('\nURL: %s' % (self.url))
        print('[*] SCRAPING LINKS... [*]\n')

        for link in soup.find_all('a'):
            print('[--] %s' % (link.get('href')))
            time.sleep(0.05)
    
    # Scrape text from the web-page.
    def text_scraper(self,):
        data = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(data, 'html.parser')
        print('\nURL: %s' % (self.url))
        print('[*] SCRAPING TEXT... [*]\n')
        print('[->] %s' % (soup.get_text()))




