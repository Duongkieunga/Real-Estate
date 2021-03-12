import scrapy
from scrapy.http import FormRequest
# from ..items import QuotetutorialItem

class QuotestoScrape(scrapy.Spider):
    name = "quotes"

    login_url = ""

    start_urls = [
        "http://quotes.toscrape.com/login"
    ]

    def parse(self, response):

        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token':token,
            'username':'admin',
            'password':'12345'
        })
        # },callback=self.start_scraping)

    # def start_scraping():
    #     items - QuotetutorialItem()

    #     all_div_quotes = response.css('div.quote')

    #     for quotes in all_div_quotes:
    #         title = quotes.css('span.text::text').extract()
    #     items['title'] = title

    #     yield items