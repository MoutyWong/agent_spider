# -*- coding: utf-8 -*-
import scrapy


class A66ipSpider(scrapy.Spider):
    name = "66ip"
    allowed_domains = ["66ip.cn"]
    start_urls = (
        'http://www.66ip.cn/',
    )

    def parse(self, response):
        pass
