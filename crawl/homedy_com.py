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
    page_idx=1
    def __init__(self, homePage, url):
        self.homePage = homePage
        self.pages = set()
        self.nPages = 0
        self.url = url
        self.path = "/home/nga/Documents/20193/Project/request/Datas"

        try:
            setPages = codecs.open(self.path+'/'+self.homePage+'.txt', 'r', 'utf-8')
            self.pages = set(line[:-1] for line in setPages.readlines())
            setPages.close()
            self.nPages = len(self.pages)
        except:

            os.makedirs(self.path+'/'+ self.homePage, exist_ok = True)
            # os.makedirs(self.path+'/request/Datas/'+ self.homePage, exist_ok = True)
        
        self.pathData = self.path+'/'+ self.homePage
            
    def getPages(self, url):

        html = requests.get('https://'+self.homePage+url).text
        return BeautifulSoup(html, 'html.parser')
        
    def savePages(self, contents):
        # print(contents)
        with codecs.open(self.path+'/'+self.homePage+'.txt', 'a', 'utf-8') as filePage:
            for content in contents:
                page = "/"+content.find("a")['href']
                # print(page)
                # continue
                if page not in self.pages:
                    bs = self.getPages(page)
                    if bs is not None:
                        self.nPages += 1
                        
                        with codecs.open(self.path+'/'+self.homePage+'/'+str(self.nPages)+'.html', 'w', 'utf-8') as f:
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
            try:
                self.savePages(bs.find("div",{"class":"tab-content"}).find_all("h3"))
            except:
                with open("homedy_com.txt","a") as f:
                    f.write(url+"\n")
            self.page_idx+=1
            self.crawl('/ban-nha-dat-ha-noi/p'+str(self.page_idx))
        
url = '/ban-nha-dat-ha-noi/p100'
c = Crawler('homedy.com',url)         
c.crawl(url)