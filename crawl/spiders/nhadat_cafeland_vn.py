import scrapy, re, requests, base64, time, os
from scrapy import FormRequest
from scrapy import Request

class Nhadat_cafeland_vn(scrapy.Spider):
    name ="nhadat.cafeland.vn"
    homepage = "nhadat.cafeland.vn"

    start_urls = ["https://nhadat.cafeland.vn/ban-nhanh-nha-dep-danh-cho-tay-o-5-tang-pho-ho-tung-mau-cau-giay-ha-noi-40m2-1493430.html"]
    
    def __init__(self):
        self.set_link = list()
        try:
            with open('../request/'+self.homepage+'.txt','r') as f:
                for link in f.readlines():
                    self.set_link.append(link)
        except:
            f = open('../request/'+self.homepage+'.txt','w')
            f.close()
        self.set_line = sorted(self.set_link)
        self.n_set_link = len(self.set_link)
        # print(self.n_set_link)

        self.n_Pages = 0
    
    def parse(self, response):
        print('\n\n\n---------------------------------------------------------\n\n\n')
        print(os.getcwd())
        with open('../request/'+self.homepage+'.html','w') as f:
            f.write(response.body.decode('utf-8'))
        return
    #     with open('../request/'+self.homepage'.txt','a') as f:
    #         for link in response.xpath("//div[@class='list-group list-search-result-group tlp headline']/descendant::a[@target='_blank']/@href").getall():
    #             # print(link)
    #             if link not in self.set_careerlink:
    #                 # print(link)
    #                 f.write(link+'\n')
    #                 yield Request(url=self.homepage+link, callback=self.savePages)
    #                 # pass
                    
                    
    #     # return
    #     # print('\n\n\n-----------------------------\n\n\n')
    #     next_page = list(response.xpath("//ul[@class='pagination']/descendant::a/@href"))[-1].get()
    #     # print(next_page)
    #     self.nPages +=1
    #     # print(self.nPages)
    #     yield Request(self.homepage+next_page,callback=self.parse)
        

    # def savePages(self, response):
    #     with open('spiders/data/careerlink/'+str(self.n_set_careerlink+1)+'.html','w') as f:
    #         f.write(response.body.decode('utf8'))
    #         self.n_set_careerlink+=1

# 7600


        