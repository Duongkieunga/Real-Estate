import scrapy, re, requests, base64, time, os
from scrapy import FormRequest
from scrapy import Request
print(os.getcwd())
class Batdongsan(scrapy.Spider):
    name ="batdongsan1"
    homepage = "https://batdongsan.com.vn"

    start_urls = [
        "https://www.batdongsan.com.vn/nha-dat-ban-ha-noi"
    ]
    
    def __init__(self):
        self.set_link = list()
        with open('./crawl/set/bds_com_vn.txt','r') as f:
            for link in f.readlines():
                self.set_link.append(link.split('\n')[0])
                # print(link.rsplit('\n')[0])
        self.n_set_link = len(self.set_link)

        self.n_Pages = 0
    
    def start_requests1(self, url):
        return Request(url=url, callback=self.parse)

    def parse(self, response):
        # return
        if len(list(response.xpath("//div[@class='pagination']/a/@href"))) ==0:
            return self.start_requests1(str(response.url))
        
        # print('\n\n\n-----------------------------\n\n\n')

        pages = list(response.xpath("//div[@class='pagination']/a"))
        nPages = len(pages)
        for i in range(nPages) :
            if pages[i].xpath('@class').get() == 'actived':
                if nPages-i>2:
                    for j in range(i, nPages-2):
                        time.sleep(4)
                        print('-',self.homepage+pages[j].xpath('@href').get())
                        # pa.write(pages[j].xpath('@href').get()+"\n")
                        yield Request(url=self.homepage+pages[j].xpath('@href').get(),callback=self.getPages)
                        # print('-')
                        # return
                    time.sleep(4)
                    print('--',pages[nPages-2].xpath('@href').get()+"\n")
                    # pa.write(pages[nPages-2].xpath('@href').get()+"\n")
                    # yield Request(url=self.homepage+pages[nPages-2].xpath('@href').get(),callback=self.getPages)
                    yield Request(url=self.homepage+pages[nPages-2].xpath('@href').get(),callback=self.parse)
                else:
                    time.sleep(4)
                    # pa.write(pages[j].xpath('@href').get()+"\n")
                    print('---',pages[j].xpath('@href').get()+"\n")
                    yield Request(url=self.homepage+pages[i].xpath('@href').get(),callback=self.getPages)
                return

    def savePages(self, response):
        self.n_set_link+=1
        # return

        with open('./crawl/data/batdongsan/'+str(self.n_set_link)+'.html','w') as f:
            f.write(response.body.decode('utf8'))

    def getPages(self, response):
        with open('./crawl/set/bds_com_vn.txt','a') as f:
            for link in response.xpath("//h3[@class='product-title']/a/@href"):
                # print(self.homepage+link.get())
                # continue
                if link.get() not in self.set_link:
                    f.write(link.get()+'\n')
                    # yield Request(url=self.homepage+link.get(), callback=self.savePages)
                # return


        