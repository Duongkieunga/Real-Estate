# !pip install scrapy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse, quote # use the urllib.parse.quote function on the non-ascii string
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import ssl, os, codecs, re
import base64, requests


class Crawler:
    count = 0
    idx_page = 1
    def __init__(self, homePage, url):
        self.homePage = homePage
        self.pages = set()
        self.nPages = 0
        self.url = url
        self.path = os.path.abspath(os.getcwd())

        try:
            setPages = codecs.open(self.path+'/'+self.homePage+'.txt', 'r', 'utf-8')
            self.pages = set(line[:-1] for line in setPages.readlines())
            setPages.close()
            self.nPages = len(self.pages)
        except:

            os.makedirs(self.path+'/'+ self.homePage, exist_ok = True)
        
        self.pathData = self.path+'/'+ self.homePage
            
    def getPages(self, url):
        html = requests.get(url).text
        return BeautifulSoup(html, 'html.parser')
        
    def savePages(self, contents):
        with codecs.open(self.path+'/'+self.homePage+'.txt', 'a', 'utf-8') as filePage:
            for content in contents:
                page = content.find("a")['href']
                if page not in self.pages:
                    bs = self.getPages(page)
                    if bs is not None:
                        self.nPages += 1
                        with codecs.open('./'+self.homePage+'/'+str(self.nPages)+'.html', 'w', 'utf-8') as f:
                            f.write(bs.prettify())
                            self.count +=1
                        self.pages.add(page)
                        filePage.write(page+'\n')
                        print(self.nPages)
                        print(page)
        
    def crawl(self, url):
        bs = self.getPages(url)
        if bs is not None:
            self.savePages(bs.find_all("div",{"class":"caption_wrapper"}))
        self.idx_page +=1
        self.crawl('https://vndiaoc.com/can-ban-ha-noi.html/?p='+str(self.idx_page)+'&sort=0')

url = 'https://vndiaoc.com/can-ban-ha-noi.html/?p=1&sort=0'
c = Crawler('vndiaoc.com',url)         
c.crawl(url)