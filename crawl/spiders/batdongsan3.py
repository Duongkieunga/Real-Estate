import scrapy, re, requests, base64, time, os
from scrapy import FormRequest
from scrapy import Request

class Batdongsan(scrapy.Spider):
    name ="batdongsanggdrive"
    homepage = "https://batdongsan.com.vn"

    start_urls = ["https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-dong"]
    
    def __init__(self):
        self.set_link = list()
        with open('set/set_bds_chungcu1.txt','r') as f:
            for link in f.readlines():
                self.set_link.append(link)
        self.set_line = sorted(self.set_link)
        self.n_set_link = len(self.set_link)
        # print(self.n_set_link)

        self.n_Pages = 0
    
    def start_requests1(self, url, i):
        return Request(url=url, callback=self.parse1, meta={"i":i+1})

    def parse(self, response):
        # print('\n\n\n-----------------------------\n\n\n')
        for i in range(1,self.n_set_link):
            if not os.path.isfile("data/batdongsan/chungcu/"+str(i)+".html"):
                time.sleep(3)
                yield self.start_requests1(self.homepage+self.set_link[i], i)
            # return
    def parse1(self, response):
        k = response.meta["i"]-1
        with open('data/batdongsan/chungcu/'+str(k)+".html","w") as f:
            f.write(response.body.decode('utf8'))


# 7600


        