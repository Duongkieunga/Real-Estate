import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class FirstSpider(scrapy.Spider):

    name = "first"

    def __init__(self, group = None, *args, **kwargs):
        super(FirstSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["https://secure.vietnamworks.com/login/vi?client_id=3"]

    