import scrapy
from scrapy import FormRequest
from scrapy import Request

class Jobstreet(scrapy.Spider):
    name ="jobstreet"
    homepage = "https://www.jobstreet.vn"

    start_urls = ["https://www.jobstreet.vn/j?q=&l=&sp=homepage#email_alert_modal"]

    def __init__(self):
        self.set_jobstreet = set()
        with open('spiders/set_jobstreet.txt','r') as f:
            for jobstreet in f.readlines():
                self.set_jobstreet.add(jobstreet)
        self.n_set_jobstreet = len(self.set_jobstreet)

        self.nPages = 0


    def parse(self, response):
        # print('\n\n\n-----------------------------\n\n\n')
        # with open('spiders/jobstreet/jobstreet.html','w') as f:
        #     f.write(response.body.decode('utf-8'))
        with open('spiders/set_jobstreet.txt','a') as f:
            for link in response.xpath("//li[@class='result']/descendant::a[1]/@href").getall():
                if link not in self.set_jobstreet:
                    f.write(link+'\n')
                    yield Request(url=self.homepage+link, callback=self.savePages)
                    pass
                    
                    
        next_page = response.xpath("//div[@class='pagination']/a[@class='next_page next trackable']/@href").get()
        # print(next_page)
        self.nPages +=1
        # print(self.nPages)
        yield Request(self.homepage+next_page,callback=self.parse)
        

    def savePages(self, response):
        with open('spiders/jobstreet/'+str(self.n_set_jobstreet+1)+'.html','w') as f:
            f.write(response.body.decode('utf8'))
            self.n_set_jobstreet+=1


        