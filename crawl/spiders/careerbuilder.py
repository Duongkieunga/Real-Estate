import scrapy
from scrapy import FormRequest
from scrapy import Request

class Careerbuilder(scrapy.Spider):
    name ="careerbuilder"

    start_urls = ["https://careerbuilder.vn/viec-lam/tat-ca-viec-lam-vi.html"]

    def __init__(self):
        self.set_link = set()
        with open('spiders/set/set_link.txt','r') as f:
            for link in f.readlines():
                self.set_link.add(link)
        self.n_set_link = len(self.set_link)

        self.nPages = 0


    def parse(self, response):
        # print('\n\n\n-----------------------------\n\n\n')
        with open('spiders/set/set_link.txt','a') as f:
            for link in response.xpath("//div[@class='job-item  ']/descendant::a[2]/@href").getall():
                # print(link)
                if link not in self.set_link:
                    f.write(link+'\n')
                    yield Request(url=link, callback=self.savePages)
                    
                    
        # return
        next_page = response.xpath("//div[@class='pagination']/descendant::li[@class='next-page']/a/@href").get()
        self.nPages +=1
        # print(self.nPages)
        yield Request(next_page,callback=self.parse)
        

    def savePages(self, response):
        with open('spiders/data/careerbuilder/'+str(self.n_set_link+1)+'.html','w') as f:
            f.write(response.body.decode('utf8'))
            self.n_set_link+=1


        