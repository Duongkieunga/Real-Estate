import scrapy
import logging
from scrapy import FormRequest

def authentication_failed(response):
    if "Error" in response.body:
        return True
    if "Invalid login or password" in response.body:
        return True
    return False

class Vietnamworks(scrapy.Spider):

    name = "vietnamworks"
    start_urls = ["https://secure.vietnamworks.com/login/vi?client_id=3"]

    def parse(self, response):

        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            '_token':token,
            'username':'duongkieunga9928@gmail.com',
            'password':'A2123456'
        }, callback = self.start_scraping)
    
    def start_scraping(self, response):

        if authentication_failed(response):
            self.logger.error("Login failed")
            return
        logging.log(logging.INFO,'Logged in and start parsing')

        url_page = "https://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam"
        yield scrapy.Request(url=url_page,
            callback=self.crawl)
    
    def crawl(self, response):
        pass


        