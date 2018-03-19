#!/usr/bin/python
import sys
import urllib.request
from html.parser import HTMLParser
import os.path
import time

class GithubSearchParser(HTMLParser):
    GITHUB_BASE_URL = "https://github.com"
    GITHUB_SEARCH_URL_ADDON = "/search?utf8=%E2%9C%93&q="
    GITHUB_SEARCH_URL_ADDON_ASC = "/search?o=asc&utf8=%E2%9C%93&q="
    GITHUB_SEARCH_URL_ADDON_STARS = "/search?o=desc&s=stars&type=Repositories&utf8=%E2%9C%93&q="
    GITHUB_SEARCH_URL_ADDON_FSTARS = "/search?o=asc&s=stars&type=Repositories&utf8=%E2%9C%93&q="
    GITHUB_SEARCH_URL_ADDON_FORKS = "/search?o=desc&s=forks&type=Repositories&utf8=%E2%9C%93&q="
    GITHUB_SEARCH_URL_ADDON_FFORKS = "/search?o=asc&s=forks&type=Repositories&utf8=%E2%9C%93&q="
    GITHUB_SEARCH_URL_ADDON_UPDATED = "/search?o=desc&s=updated&type=Repositories&utf8=%E2%9C%93&q="
    GITHUB_SEARCH_URL_ADDON_FUPDATED = "/search?o=asc&s=updated&type=Repositories&utf8=%E2%9C%93&q="
    GITHUB_SEARCH_ADDONS = [
        GITHUB_SEARCH_URL_ADDON,
        GITHUB_SEARCH_URL_ADDON_ASC,
        GITHUB_SEARCH_URL_ADDON_STARS,
        GITHUB_SEARCH_URL_ADDON_FORKS,
        GITHUB_SEARCH_URL_ADDON_UPDATED
    ]

    TIMEOUT = 3
    in_link_block = False
    next_page = ""

    def mine_tech(self, tech):
        self.ofile = open(tech, 'a+')
        for search_addon in self.GITHUB_SEARCH_ADDONS:
            self.mine_url(self.GITHUB_BASE_URL + search_addon + tech)
            while(self.next_page != ""):
                time.sleep(self.TIMEOUT)
                self.mine_url(self.GITHUB_BASE_URL + self.next_page)

    def mine_url(self, url):
        print("[*] mining url: " + url)
        self.next_page = ""
        try:
            self.feed(str(urllib.request.urlopen(url).read()))
        except urllib.error.HTTPError as err:
            print("[!] got an error: " + str(err))
            time.sleep(250)
            # self.feed(str(urllib.request.urlopen(url).read()))
            self.mine_url(url)

    def handle_starttag(self, tag, attrs):
        if(self.in_link_block == True):
            if(tag == "a"):
                for attr in attrs:
                    if(attr[0] == "href"):
                        print("[->] link found: " + attr[1])
                        self.ofile.write(attr[1] + "\n")
                        self.in_link_block = False
        for attr in attrs:
            if(attr[1] == 'repo-list-item d-flex flex-justify-start py-4 public source'):
                self.in_link_block = True
            elif(attr[1] == 'next_page'):
                for a in attrs:
                    if(a[0] == 'href'):
                        self.next_page = a[1]

parser = GithubSearchParser()

for arg in sys.argv:
    if(arg != 'scrape-github.py'):
        parser.mine_tech(arg)
