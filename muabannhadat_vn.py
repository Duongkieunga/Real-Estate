# !pip install scrapy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse, quote # use the urllib.parse.quote function on the non-ascii string
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import ssl, os, codecs, re
from PIL import Image
import base64, requests
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class Crawler:
    count = 0
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

        html = requests.get('https://www.'+self.homePage+url).text
        return BeautifulSoup(html, 'html.parser')
        
    def savePages(self, contents):

        with codecs.open(self.path+'/'+self.homePage+'.txt', 'a', 'utf-8') as filePage:
            for content in contents[1:]:
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
                        # return
                        
                        print(self.nPages)
                        print(page)
        
    def crawl(self, url):
        bs = self.getPages(url)
        if bs is not None:
            self.savePages(bs.find_all("h3",{"class":"uppercase text-red text-base leading-normal mb-1"}))
        pages = bs.find("ul",{"class":"pagination"}).find_all("a")
        self.crawl(pages[-1].attrs['href'])
url = '/mua-ban-bat-dong-san/tp-ha-noi'
c = Crawler('muabannhadat.vn',url)         
c.crawl(url)