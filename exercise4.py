try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import os.path
import requests
import urllib.parse


def twitter_info(url):
    if not 'twitter.com' in url:
        raise ValueError("Twitter url must be => https://twitter.com/xxxxxx")

    path = urllib.parse.urlparse(url).path

    # finding unique url account
    account_url = ''
    checking_url = path
    while True:
        checking_url, splited_url = os.path.split(checking_url)
        if checking_url == '/':
            account_url = splited_url
            break
        elif checking_url == '':
            raise ValueError("Twitter url must be => https://twitter.com/xxxxxx")
            
    f = requests.get("https://twitter.com/{}".format(account_url))
    soup = BeautifulSoup(f.content, features="html.parser")

    print(soup.title.text)
    print(soup.body.find('a', attrs={'href':'/{}/followers'.format(account_url)}).get('title'))


if __name__== "__main__":
    twitter_info("https://twitter.com/KMbappe")
    # print("--------------------------")
    # twitter_info("https://google.com")
    # print("--------------------------")
    # twitter_info("https://twitter.com")
    print("--------------------------")
    twitter_info("https://twitter.com/VirgilvDijk/media")
    print("--------------------------")
    twitter_info("https://twitter.com/YoobaoT/")
