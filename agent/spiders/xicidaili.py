# -*- coding: utf-8 -*-
import scrapy


class XicidailiSpider(scrapy.Spider):
    name = "xicidaili"
    allowed_domains = ["xicidaili.com"]
    start_urls = (
        'http://www.xicidaili.com/',
    )

    def parse(self, response):
        pass
