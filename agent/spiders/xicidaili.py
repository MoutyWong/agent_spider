# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from agent.items import AgentItem
import re

class XicidailiSpider(scrapy.Spider):
	name = "xicidaili"
	allowed_domains = ["xicidaili.com"]
	start_urls = (
		'http://www.xicidaili.com/wn/',
		# 'http://www.xicidaili.com/nn/',
		)
		
	handle_httpstatus_list = [500]
# 国内高匿 http://www.xicidaili.com/nn/1
# 国外高匿 http://www.xicidaili.com/wn/1
	def parse(self, response):
		agent_ip = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[2]/text()").extract()
		agent_port = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[3]/text()").extract()
		agent_position = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[4]/text()").extract()
		print(agent_position)
		for i in range(len(agent_position)):
			item = AgentItem()
			item['ip'] = agent_ip[i]
			item['port'] = agent_port[i]
			item['position'] = re.sub(r'\n+|\s+','',agent_position[i]) 
			item['origin'] = self.name
			yield item

		print('-------------------------------------------------------', response.url)
		
		for i in range(2, 21):
			next_url_wn = self.start_urls[0] + str(i)
			yield Request(next_url_wn, callback=self.wn_parse)
		for i in range(1,21):
			next_url_nn = 'http://www.xicidaili.com/nn/' + str(i)
			yield Request(next_url_nn, callback=self.nn_parse)
		
		
	def wn_parse(self, response):
		agent_ip = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[2]/text()").extract()
		agent_port = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[3]/text()").extract()
		agent_position = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[4]/text()").extract()
		for i in range(len(agent_position)):
			item = AgentItem()
			item['ip'] = agent_ip[i]
			item['port'] = agent_port[i]
			item['position'] = re.sub(r'\n+|\s+','',agent_position[i])
			item['origin'] = self.name
			yield item
		print('-------------------------------------------------------', response.url)
	
	def nn_parse(self, response):
		agent_ip = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[2]/text()").extract()
		agent_port = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[3]/text()").extract()
		agent_position = response.xpath("//table[@id='ip_list']//tr[position()>1]/td[4]/a/text()").extract()
		for i in range(len(agent_position)):
			item = AgentItem()
			item['ip'] = agent_ip[i]
			item['port'] = agent_port[i]
			item['position'] = re.sub(r'\n+|\s+','',agent_position[i])
			item['origin'] = self.name
			yield item
		print('-------------------------------------------------------', response.url)