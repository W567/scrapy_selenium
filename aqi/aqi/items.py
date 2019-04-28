# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	city = scrapy.Field()
	date = scrapy.Field()
	AQI = scrapy.Field()
	level = scrapy.Field()
	pm2_5 = scrapy.Field()
	pm10 = scrapy.Field()
	level = scrapy.Field()
	pass
