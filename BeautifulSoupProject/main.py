#!/usr/bin/env python

# Imported dependencies. The code WILL not function as intended -
# if one of the modules is removed.
from bs4 import BeautifulSoup
from colorama import init, Fore
from urllib.error import HTTPError, URLError
import time
import urllib.request


class WebsiteScraper:
    # Colorama requires the init function to be called before use.
    init()            
    
    # The linkScraper() method has one main argument (url). This method scrapes links -
    # from a specified web-page.
    def link_scraper(self, url, ratelimit,):
        try:
            # urlopen() sends a request to the specified url. The timeout argument (measured in seconds) has been specific -
            # in the case of a the request taking more time than needed.
            data = urllib.request.urlopen(url, timeout=15)
            soup = BeautifulSoup(data, 'html.parser')
            print(Fore.LIGHTCYAN_EX + '\nURL: %s' % (url))
            print(Fore.LIGHTCYAN_EX + 'Timeout limit: 15s')
            print(Fore.LIGHTGREEN_EX + '[+] SCRAPING LINKS... [*]\n')
            
            # A for loop used to loop through the "a" element tags in a web-page -
            # the link.get() method then searches for a specific attribute ('href').
            for link in soup.find_all('a'):
                link_check = str(link.get('href'))
                
                # Differentiate between a path and a link with a simple -
                # conditional statement.
                if link_check.startswith('/'):
                    print('[+] Path: %s' % link_check)
                elif link_check == str(None) or link_check == '':
                    print('[-] Link/Path: Cannot detect <href> value')
                else:
                    print('[+] Link: %s' % link_check)
                    

                time.sleep(ratelimit)
        except (HTTPError, URLError, TimeoutError, ConnectionError) as err:
            print('Error reason: %s' % (err.reason))
            print('Error code: %d' % (err.code))
    

    # Scrape text from the web-page. The same method of grabbing, and -
    # scraping web-page data as linkScraper().
    def text_scraper(self, url, ratelimit,):
        try:
            data = urllib.request.urlopen(url, timeout=15)
            soup = BeautifulSoup(data, 'html.parser')
            print(Fore.LIGHTCYAN_EX + '\nURL: %s' % (url))
            print(Fore.LIGHTCYAN_EX + 'Timeout limit: 15s')
            print('[+] SCRAPING TEXT... [+]\n')
            
            # Due to the way BS4 scrapes text it leaves tons of whitespaces -
            # to negate this I've used a for loop that loops through a method that removes -
            # the whitespaces.
            for string in soup.stripped_strings:
                print(Fore.LIGHTGREEN_EX + '[+] %s' % (repr(string)))
                time.sleep(ratelimit)
        except (HTTPError, URLError, TimeoutError, ConnectionError) as err:
            print('Error reason: %s' % (err.reason))
            print('Error code: %d' % (err.code))



# Initiates an instance of the WebsiteScraper class. 
# Prints the usage for the user.
if __name__ == '__main__':
    print('''Usage: sl - [scrape web-page links]
       st - [scrape web-page text]''')
    
    instance = WebsiteScraper()    
    mode = input('Enter mode >>>  ')
    url = input('URL >>> ')
    ratelimit = int(input('Specify your rate limit >>> '))
    if mode == 'sl':
        instance.link_scraper(url, ratelimit)
    elif mode == 'st':
        instance.text_scraper(url, ratelimit)
    else:
        print('Error occurred..')
