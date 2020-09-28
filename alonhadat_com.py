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
    page_index =70
    def __init__(self, homePage, url):
        self.homePage = homePage
        self.pages = set()
        self.nPages = 0
        self.url = url
        self.path = os.path.abspath(os.getcwd())

        try:
            setPages = codecs.open(self.path+'/crawl/'+self.homePage+'.txt', 'r', 'utf-8')
            self.pages = set(line[:-1] for line in setPages.readlines())
            setPages.close()
            self.nPages = len(self.pages)
        except:
            setPages = codecs.open(self.path+'/crawl/'+self.homePage+'.txt', 'w', 'utf-8')
            setPages.close()
            os.makedirs(self.path+'/Datas/'+ self.homePage, exist_ok = True)
        
        self.pathData = self.path+'/Datas/'+ self.homePage
            
    def getPages(self, url):
        html = requests.get('http://'+self.homePage+url).text
        return BeautifulSoup(html, 'html5lib')
        
    def savePages(self, contents):
        # print('\n------------------------------------------------------------------\n')
        with codecs.open(self.path+'/crawl/'+self.homePage+'.txt', 'a', 'utf-8') as filePage:

            for content in contents:
                page = content.find('a')['href']

                if page not in self.pages:
                    bs = self.getPages(page)
                    if bs is not None:
                        with codecs.open('./Datas/'+self.homePage+'/'+str(self.nPages+1)+'.html', 'w', 'utf-8') as f:
                            f.write(bs.prettify())
                            self.count +=1
                        self.pages.add(page)
                        filePage.write(page+'\n')
                        self.nPages += 1

        
    def crawl(self, url):
        bs = self.getPages(url)
        if bs is not None:
            self.savePages(bs.find_all('div',{'class':'ct_title'})) 
            self.page_index+=1  
            print(self.page_index)
            self.crawl('/nha-dat/can-ban/nha-dat/1/ha-noi/trang--'+str(self.page_index)+'.html')
url = '/nha-dat/can-ban/nha-dat/1/ha-noi/trang--70.html'
c = Crawler('alonhadat.com.vn',url)         
c.crawl(url)