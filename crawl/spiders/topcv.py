import scrapy, re
from scrapy import FormRequest
from scrapy import Request

class Topcv(scrapy.Spider):
    name ="topcv"

    start_urls = ["https://www.topcv.vn/tim-viec-lam-moi-nhat"]

    def __init__(self):
        self.set_topcv = set()
        with open('spiders/set_topcv.txt','r') as f:
            for link in f.readlines():
                self.set_topcv.add(link)
        self.n_set_topcv = len(self.set_topcv)

        self.nPages = 0



    def parse(self, response):
        # with open("spiders/topcv/topcv.html",'w') as f:
            # f.write(response.body.decode('utf8'))
        # print('\n\n\n-----------------------------\n\n\n')
        with open('spiders/set_topcv.txt','a') as f:
            for link in response.xpath("//h4[@class='job-title']/a/@href").getall():
                # print(link)
                if link not in self.set_topcv:
                    f.write(link+'\n')
                    yield Request(url=link, callback=self.savePages)
                    
                    
        # return
        next_page = response.xpath("//ul[@class='pagination']/descendant::a[@rel='next']/@href").get()
        # print(next_page)
        self.nPages +=1
        # print(self.nPages)
        yield Request(next_page,callback=self.parse)
        

    def savePages(self, response):
        with open('spiders/topcv/'+str(self.n_set_topcv+1)+'.html','w') as f:
            f.write(response.body.decode('utf8'))
            self.n_set_topcv+=1
            # pass


        