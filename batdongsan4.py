import scrapy, re, requests, base64, time, os
from scrapy import FormRequest
from scrapy import Request

class Batdongsan(scrapy.Spider):
    name ="batdongsan2"
    homepage = "https://batdongsan.com.vn"

    start_urls = []
    
    def __init__(self):
        with open('./crawl/set/bds_com_vn.txt','r') as f:
            for link in f.readlines():
                self.start_urls.append(link.split('\n')[0])
    
    def start_requests(self):
        print('\n\n---------------------------\n\n')
        for i in range(len(self.start_urls)):
            time.sleep(3)
            yield Request(url=self.homepage+self.start_urls[i], callback=self.parse, meta={"i":i+1})

    def parse(self, response):
        k = response.meta["i"]
        # print('\n------------------------',k)
        with open('./crawl/data/batdongsan/'+str(k)+".html","w") as f:
            f.write(response.body.decode('utf8'))

        