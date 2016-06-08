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
		self.cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE TYPE = 'table' AND NAME = 'agents'")
		if self.cursor.fetchone()[0] == 0:
			self.cursor.execute("CREATE TABLE agents (id INTEGER PRIMARY KEY AUTOINCREMENT, ip VARCHAR(255), port VARCHAR(255), position VARCHAR(255), origin VARCHAR(255))")
		# else:
			# self.cursor.execute("DELETE FROM agents")
			# self.cursor.execute("DELETE FROM sqlite_sequence")

	
	def process_item(self, item, spider):
		self.cursor.execute("insert into agents (ip, port, position, origin) values(?, ?, ?, ?)", (item['ip'], item['port'], item['position'], item['origin']))
		self.conn.commit()
		return item
