# -*- coding: utf8 -*-
import re

from scrapy.xpath import HtmlXPathSelector
from scrapy.item import ScrapedItem
from scrapy.link.extractors import RegexLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class CfdSpider(CrawlSpider):
    domain_name = 'ffvl.fr'
    start_urls = ['http://www.ffvl.fr/']

    rules = (
        Rule(RegexLinkExtractor(allow=(r'Items/', )), 'parse_item', follow=True),
    )

    def parse_item(self, response):
        #xs = HtmlXPathSelector(response)
        #i = ScrapedItem()
        #i.attribute('site_id', xs.x('//input[@id="sid"]/@value'))
        #i.attribute('name', xs.x('//div[@id="name"]'))
        #i.attribute('description', xs.x('//div[@id="description"]'))

SPIDER = CfdSpider()
