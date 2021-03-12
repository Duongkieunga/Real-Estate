import scrapy, re
from scrapy import FormRequest
from scrapy import Request

class Vieclam24h(scrapy.Spider):
    name ="vieclam24h"
    homepage = "https://vieclam24h.vn"
    start_urls = ["https://vieclam24h.vn/tim-kiem-viec-lam-nhanh/?hdn_tu_khoa=&hdn_nganh_nghe_cap1=&hdn_dia_diem=&key=ttv_nangcao"]

    def __init__(self):
        self.set_vieclam24h = set()
        with open('spiders/set/set_vieclam24h.txt','r') as f:
            for link in f.readlines():
                self.set_vieclam24h.add(link)
        self.n_set_vieclam24h = len(self.set_vieclam24h)
        self.n_set_vieclam24h=1347
        self.nPages = 0

    def parse(self, response):
        # with open("spiders/vieclam24h/test.html",'w') as f:
        #     f.write(response.body.decode('utf8'))
        # print('\n\n\n-----------------------------\n\n\n')
        with open('spiders/set/set_vieclam24h.txt','a') as f:
            for link in response.xpath("//span[@class='title-blockjob-main truncate-ellipsis font14 pos_relative pr_28']/a/@href").getall():
                # print(link)
                if link not in self.set_vieclam24h:
                    f.write(link+'\n')
                    yield Request(url=self.homepage+link, callback=self.savePages)
                    
        # return
        next_page = response.xpath("//ul[@class='pagination']/descendant::a[@aria-label='Next']/@href").get()
        # print(next_page)
        self.nPages +=1
        # print(self.nPages)
        yield Request(self.homepage+next_page,callback=self.parse)
        

    def savePages(self, response):
        with open('spiders/data/vieclam24h/'+str(self.n_set_vieclam24h+1)+'.html','w') as f:
            f.write(response.body.decode('utf8'))
            self.n_set_vieclam24h+=1
            # pass


        