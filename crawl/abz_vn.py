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
    page_index = 1414
    count = 0
    def __init__(self, homePage, url):
        self.homePage = homePage
        self.pages = set()
        self.nPages = 0
        self.url = url
        self.path = os.path.abspath(os.getcwd())

        try:
            setPages = codecs.open(self.path+'/request/crawl/'+self.homePage+'.txt', 'r', 'utf-8')
            self.pages = set(line[:-1] for line in setPages.readlines())
            setPages.close()
            self.nPages = len(self.pages)
        except:

            os.makedirs(self.path+'/request/Datas/'+ self.homePage, exist_ok = True)
        
        self.pathData = self.path+'/request/Datas/'+ self.homePage
            
    def getPages(self, url):
        html = requests.get(url).text
        return BeautifulSoup(html, 'html.parser')
        
    def savePages(self, contents):

        with codecs.open(self.path+'/request/crawl/'+self.homePage+'.txt', 'a', 'utf-8') as filePage:
            for content in contents:
                # try:
                page = content['href']
                # print(page)
                # continue
                # except:
                    # continue
                if page not in self.pages:
                    bs = self.getPages(page)
                    if bs is not None:
                        self.nPages += 1
                        with codecs.open('./request/Datas/'+self.homePage+'/'+str(self.nPages)+'.html', 'w', 'utf-8') as f:
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
            self.savePages(bs.find_all("a",{"class":"image-item-nhadat"}))
            self.page_index+=1
            print('\n\n-----------------------------------------------\n\n')
            print(self.page_index)
            self.crawl('https://abz.vn/danh-sach/bat-dong-san/loai-hinh:nha-dat-ban/tinh-tp:ha-noi-page'+str(self.page_index)+'.html')

url = 'https://abz.vn/danh-sach/bat-dong-san/loai-hinh:nha-dat-ban/tinh-tp:ha-noi-page1414.html'
c = Crawler('abz.vn',url)         
c.crawl(url)