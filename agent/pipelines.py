# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3

class AgentPipeline(object):
	def __init__(self):
		self.conn = sqlite3.connect('agent.db')
		self.cursor = self.conn.cursor()
		self.cursor.execute("select count(*) from sqlite_master where type = 'table' and name = 'agents'")
		if self.cursor.fetchone()[0] == 0:
			self.cursor.execute("create table agents (id integer primary key autoincrement, ip varchar(255), port varchar(255), position varchar(255), origin varchar(255))")
	
	def process_item(self, item, spider):
		self.cursor.execute("insert into agents (ip, port, position, origin) values(?, ?, ?, ?)", (item['ip'], item['port'], item['position'], item['origin']))
		self.conn.commit()
		print('-------------------------------------------------------')
		return item
