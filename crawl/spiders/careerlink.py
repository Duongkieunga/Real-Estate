import scrapy
from scrapy import FormRequest
from scrapy import Request

class Careerlink(scrapy.Spider):
    name ="careerlink"
    homepage = "https://www.careerlink.vn"
    allowed_domains=['careerlink.vn']


    start_urls = ["https://www.careerlink.vn/vieclam/list?view=headline&page=1"]

    def __init__(self):
        self.set_careerlink = set()
        with open('spiders/set/set_careerlink.txt','r') as f:
            for link in f.readlines():
                self.set_careerlink.add(link)
        self.n_set_careerlink = len(self.set_careerlink)

        self.nPages = 0


    def parse(self, response):
        
        # with open('spiders/careerlink/careerlink.html','w') as f:
        #     f.write(response.body.decode('utf-8'))
        # return
        with open('spiders/set/set_careerlink.txt','a') as f:
            for link in response.xpath("//div[@class='list-group list-search-result-group tlp headline']/descendant::a[@target='_blank']/@href").getall():
                # print(link)
                if link not in self.set_careerlink:
                    # print(link)
                    f.write(link+'\n')
                    yield Request(url=self.homepage+link, callback=self.savePages)
                    # pass
                    
                    
        # return
        # print('\n\n\n-----------------------------\n\n\n')
        next_page = list(response.xpath("//ul[@class='pagination']/descendant::a/@href"))[-1].get()
        # print(next_page)
        self.nPages +=1
        # print(self.nPages)
        yield Request(self.homepage+next_page,callback=self.parse)
        

    def savePages(self, response):
        with open('spiders/data/careerlink/'+str(self.n_set_careerlink+1)+'.html','w') as f:
            f.write(response.body.decode('utf8'))
            self.n_set_careerlink+=1


        