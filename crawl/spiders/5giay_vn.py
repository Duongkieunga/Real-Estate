import scrapy
from scrapy import Request

class _5giay(scrapy.Spider):
    name="5giay.vn"
    start_urls=["https://www.5giay.vn/forums/bat-dong-san.44/"]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url, callback=self.parse)
    
    def parse(self, response):
        print('\n\n\n---------------------------\n\n\n')
        with open("5giay_vn.html","w") as f:
            f.write(response.body.decode("utf8"))