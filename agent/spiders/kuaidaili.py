# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from agent.items import AgentItem

class KuaidailiSpider(scrapy.Spider):
	name = "kuaidaili"
	allowed_domains = ["kuaidaili.com"]
	start_urls = (
		'http://www.kuaidaili.com/free/outha/',
		'http://www.kuaidaili.com/free/inha/',
		)

# 国内高匿 http://www.kuaidaili.com/free/inha/1/
# 国外高匿 http://www.kuaidaili.com/free/outha/1/

	def parse(self, response):
		# if response.status == 200:
		print('--------------', response.url)
