import scrapy, re
from scrapy import FormRequest
from scrapy import Request
from functools import wraps
from scrapy.utils.python import get_func_args

def callback_args(f):
    args = get_func_args(f)[2:]
    @wraps(f)
    def wrapper(spider, response):
        return f(spider, response, 
            **{k:response.meta[k] for k in args if k in response.meta})
    return wrapper

class Timviecnhanh(scrapy.Spider):
    name ="timviecnhanh"
    homepage = "https://timviecnhanh.vn"

    start_urls = ["https://www.timviecnhanh.com/vieclam/timkiem?&page=25"]
    
    def __init__(self):
        self.set_timviecnhanh = list()
        with open('spiders/set/set_timviecnhanh.txt','r') as f:
            for link in f.readlines():
                self.set_timviecnhanh.append(link)
        self.n_set_timviecnhanh = len(self.set_timviecnhanh)

        self.nPages = 0



    def parse(self, response):
        # with open("spiders/timviecnhanh/timviecnhanh.html",'w') as f:
        #     f.write(response.body.decode('utf8'))
        # print('\n\n\n-----------------------------\n\n\n')
        
        for link in response.xpath("//td[@class='block-item w55']/a[1]/@href").getall():
            yield Request(url=link, callback=self.savePages, meta={'link':link})
                    
                    
        # return
        # print('++++++++++++++')
        next_page = response.xpath("//div[@class='page-navi ajax']/descendant::a[@class='next item']/@href").get()
        # print(next_page)
        self.nPages +=1
        # print(self.nPages)
        # yield Request(next_page,callback=self.parse)
        
    @callback_args
    def savePages(self, response, link):
        if link not in self.set_timviecnhanh:
            # return
            with open('spiders/set/set_timviecnhanh.txt','a') as f:
                # print(link)
                f.write(link+'\n')
                # pass
            with open('spiders/data/timviecnhanh/'+str(self.n_set_timviecnhanh+1)+'.html','w') as f:
                f.write(response.body.decode('utf8'))
                # pass
            self.n_set_timviecnhanh+=1



        