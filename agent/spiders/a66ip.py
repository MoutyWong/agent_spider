# -*- coding: utf-8 -*-
import scrapy
from agent.items import AgentItem
from scrapy.http import Request

class A66ipSpider(scrapy.Spider):
	name = "66ip"
	allowed_domains = ["66ip.cn"]
	start_urls = (
		'http://www.66ip.cn/',
	)
# http://www.66ip.cn/6.html
	def parse(self, response):
		agent_ip = response.xpath("//div[@id='main']/div/div[1]/table//tr[position()>1]/td[1]/text()").extract()
		agent_port = response.xpath("//div[@id='main']/div/div[1]/table//tr[position()>1]/td[2]/text()").extract()
		agent_position = response.xpath("//div[@id='main']/div/div[1]/table//tr[position()>1]/td[3]/text()").extract()
		for n in range(len(agent_ip)):
			item = AgentItem()
			item['ip'] = agent_ip[n]
			item['port'] = agent_port[n]
			item['position'] = agent_position[n]
			item['origin'] = self.name
			yield item
		print('========================================', response.url)
		for i in range(2,9):
			next_page_url = 'http://www.66ip.cn/' + str(i) + '.html'
			yield Request(next_page_url, callback=self.new_parse)
				
	def new_parse(self, response):
		if response.status == 200:
			agent_ip = response.xpath("//div[@id='main']/div/div[1]/table//tr[position()>1]/td[1]/text()").extract()
			agent_port = response.xpath("//div[@id='main']/div/div[1]/table//tr[position()>1]/td[2]/text()").extract()
			agent_position = response.xpath("//div[@id='main']/div/div[1]/table//tr[position()>1]/td[3]/text()").extract()
			for n in range(len(agent_ip)):
				item = AgentItem()
				item['ip'] = agent_ip[n]
				item['port'] = agent_port[n]
				item['position'] = agent_position[n]
				item['origin'] = self.name
				yield item
			print('========================================', response.url)
			
