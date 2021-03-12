# https://muaban.net/mua-ban-nha-dat-cho-thue-toan-quoc-l0-c3
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
        self.path = "/home/nga/Documents/20193/Project/request/Datas"
        try:
            setPages = codecs.open(self.path+'/request/crawl/'+self.homePage+'.txt', 'r', 'utf-8')
            self.pages = set(line[:-1] for line in setPages.readlines())
            setPages.close()
            self.nPages = len(self.pages)
        except:
            # setPages = codecs.open(self.path+'/Set Pages/'+self.homePage+'.txt', 'w', 'utf-8')
            # setPages.close()
            os.makedirs(self.path+'/'+ self.homePage, exist_ok = True)
        
        self.pathData = self.path+'/'+ self.homePage
            
    def getPages(self, url):

        html = requests.get(url).text
        return BeautifulSoup(html, 'html.parser')
        
    def savePages(self, contents):
        with codecs.open(self.path+'/'+self.homePage+'.txt', 'a', 'utf-8') as filePage:
            for content in contents:
                page = content.find('a',{'class':'list-item__link'})['href']

                if page not in self.pages:
                    bs = self.getPages(page)
                    if bs is not None:
                        self.nPages += 1
                        # save html
                        with codecs.open(self.path+'/'+self.homePage+'/'+str(self.nPages)+'.html', 'w', 'utf-8') as f:
                            f.write(bs.prettify())
                            self.count +=1
                        self.pages.add(page)
                        filePage.write(page+'\n')
                        
                        print(self.nPages)
                        print(page)
        
    def crawl(self, url):
        bs = self.getPages(url)
        if bs is not None:
            self.savePages(bs.find("div",{"id":"list-box"}).find_all('div', {'class':'list-item-container'}))
            pages = bs.find("div",{"class":"pagination"}).find_all("a")
            self.crawl(pages[-1].attrs['href'])
url = 'https://muaban.net/mua-ban-nha-dat-cho-thue-ha-noi-l24-c3'
c = Crawler('muaban.net',url)         
c.crawl(url) 