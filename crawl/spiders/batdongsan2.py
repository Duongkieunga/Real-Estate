import scrapy, re, requests, base64
from scrapy import FormRequest
from scrapy import Request

class Batdongsan2(scrapy.Spider):
    name ="batdongsan2"
    homepage = "https://batdongsan.com.vn"

    start_urls = ["https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-noi"]
    
    def __init__(self):
        self.set_link = list()
        with open('spiders/set/set_bds_chungcu.txt','r') as f:
            for link in f.readlines():
                self.set_link.append(link)
        self.n_set_link = len(self.set_link)
        # print(self.n_set_link)
    
    def start_requests1(self, url):
        return Request(url=url, callback=self.parse)

    def parse(self, response):
       
        list_links = []

        with open('spiders/set/batdongsan.com.vn.txt',"r") as f:
            for line in f.readlines():
                list_links.append(line)
        # print(len(list_links))
        links = []
        with open('spiders/set/set_bds_chungcu.txt',"r") as f:
            for line in f.readlines():
                if line not in list_links:
                    links.append(line)
        # print(self.n_set_link)
        # print(len(links), len(set(links)))
        # return
        with open('spiders/set/set_bds_chungcu.txt',"a") as f1:
            for link in links:
                # print(link)
                f1.write(link)
                self.n_set_link +=1
                yield Request(url=self.homepage+link,callback=self.saveHtml, meta={"idx":self.n_set_link})
                
    def saveHtml(self, response):
        # print(response.meta["idx"])
        with open('spiders/data/batdongsan/chungcu/'+str(response.meta["idx"])+'.html','w') as f:
            f.write(response.body.decode('utf8'))


        