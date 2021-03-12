import scrapy, re, requests, base64
from scrapy import FormRequest
from scrapy import Request

class Batdongsan(scrapy.Spider):
    name ="batdongsan"
    homepage = "https://batdongsan.com.vn"

    start_urls = [
        # "https://batdongsan.com.vn/ban-can-ho-chung-cu-hoan-kiem"
    # "https://batdongsan.com.vn/ban-can-ho-chung-cu-ba-dinh"
    "https://batdongsan.com.vn/ban-can-ho-chung-cu-dong-da"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-hai-ba-trung"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-thanh-xuan"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-tay-ho"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-cau-giay"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-hoang-mai"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-long-bien"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-nam-tu-liem"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-bac-tu-liem"
    # ,"https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-dong"
    ]
    
    def __init__(self):
        self.set_link = list()
        with open('../set/set_bds_chungcu.txt','r') as f:
            for link in f.readlines():
                self.set_link.append(link)
        self.n_set_link = len(self.set_link)
        # print(self.n_set_link)

        self.n_Pages = 0

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url=url, callback=self.parse)
    
    def start_requests1(self, url):
        return Request(url=url, callback=self.parse)

    def parse(self, response):
        if len(list(response.xpath("//div[@class='pagination']/a/@href"))) ==0:
            return self.start_requests1(str(response.url))
        
        # print('\n\n\n-----------------------------\n\n\n')

        pages = list(response.xpath("//div[@class='pagination']/a"))
        nPages = len(pages)
        with open("pages.txt","a") as pa:
            for i in range(nPages) :
                if pages[i].xpath('@class').get() == 'actived':
                    if nPages-i>2:
                        for j in range(i, nPages-2):
                            # print(nPages)
                            # print('-',self.homepage+pages[j].xpath('@href').get())
                            pa.write(pages[j].xpath('@href').get()+"\n")
                            yield Request(url=self.homepage+pages[j].xpath('@href').get(),callback=self.getPages)
                            # print('-')
                            # return
                        # print('--',pages[nPages-2].xpath('@href').get()+"\n")
                        pa.write(pages[nPages-2].xpath('@href').get()+"\n")
                        # yield Request(url=self.homepage+pages[nPages-2].xpath('@href').get(),callback=self.getPages)
                        yield Request(url=self.homepage+pages[nPages-2].xpath('@href').get(),callback=self.parse)
                    else:
                        pa.write(pages[j].xpath('@href').get()+"\n")
                        # print('---',pages[j].xpath('@href').get()+"\n")
                        yield Request(url=self.homepage+pages[i].xpath('@href').get(),callback=self.getPages)
                    return

    def savePages(self, response):
        self.n_set_link+=1
        # return

        with open('../data/batdongsan/chungcu/'+str(self.n_set_link)+'.html','w') as f:
            f.write(response.body.decode('utf8'))

    def getPages(self, response):
        with open('../set/set_bds_chungcu.txt','a') as f:
            for link in response.xpath("//h3[@class='product-title']/a/@href"):
                # print(self.homepage+link.get())
                pass
                f.write(link.get()+'\n')
                yield Request(url=self.homepage+link.get(), callback=self.savePages)
                # return


        