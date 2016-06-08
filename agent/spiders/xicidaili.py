# -*- coding: utf-8 -*-
import scrapy


class XicidailiSpider(scrapy.Spider):
	name = "xicidaili"
	allowed_domains = ["xicidaili.com"]
	start_urls = (
		'http://www.xicidaili.com/wn/',
		# 'http://www.xicidaili.com/nn/1',
		)
		
	handle_httpstatus_list = [500]
# 国内高匿 http://www.xicidaili.com/nn/1
# 国外高匿 http://www.xicidaili.com/wn/1
	def parse(self, response):
		print('---------------------------------', response.url, response.status)
		data = response.xpath("//*[@id='ip_list']//tr[2]/td[2]")
		print(data)