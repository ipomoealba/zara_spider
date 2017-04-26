# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZaraItem(scrapy.Item):

    cloth_class = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_img = scrapy.Field()
