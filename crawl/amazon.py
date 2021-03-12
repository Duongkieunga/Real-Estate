# !pip install scrapy
from urllib.parse import urljoin
from urllib.parse import urlparse, quote # use the urllib.parse.quote function on the non-ascii string
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import ssl, os, codecs, re
from PIL import Image
import base64, requests
# Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()
class Crawler:
    count = 0
    idx_page = 1
    headers={
    'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    def __init__(self, homePage):
        self.homePage = homePage
        self.pages = set()
        self.nPages = 0
        self.path = "/home/nga/Documents/20193/Project/request/Datas"

        try:
            setPages = codecs.open(self.path+'/'+self.homePage+'.txt', 'r', 'utf-8')
            self.pages = set(line[:-1] for line in setPages.readlines())
            setPages.close()
            self.nPages = len(self.pages)
        except:

            os.makedirs(self.path+'/'+ self.homePage, exist_ok = True)
        
        self.pathData = self.path+'/'+ self.homePage
            
    def getPages(self, url):
        html = requests.get(url, headers=self.headers, verify=False).text
        bs = BeautifulSoup(html, 'html.parser')
        print(bs)
        # while bs is None:
        #     print('---')
        #     html = requests.get(url, headers=self.headers, verify=False).text
        #     bs = self.getPages(url)
        return BeautifulSoup(html, 'html.parser')
        
    def savePages(self, contents):
        # print(len(contents))
        # return
        with codecs.open(self.path+'/'+self.homePage+'.txt', 'a', 'utf-8') as filePage:
            for content in contents:
                # try:
                page = content.find("a")['href']
                # print(page)
                # continue
                # except:
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
        print('--')
        bs = self.getPages(url)
        if bs is not None:
            categories = bs.find("ul",{"aria-labelledby":"n-title"}).find_all("li")[1:]
            father_dir = categories[0].find("span",{"dir":"auto"}).text
            print(father_dir)
        # self.idx_page +=1
        # print('/ban/ha-noi?sortby=newest&page='+str(self.idx_page))
        # self.crawl('/ban/ha-noi?sortby=newest&page='+str(self.idx_page))

url = 'https://www.amazon.com/s?i=stripbooks&bbn=1000&rh=n%3A283155%2Cn%3A5%2Cp_n_feature_nine_browse-bin%3A3291437011&dc&qid=1603841055&rnid=1000&ref=sr_nr_n_8'
c = Crawler('amazon.com')         
c.crawl(url)