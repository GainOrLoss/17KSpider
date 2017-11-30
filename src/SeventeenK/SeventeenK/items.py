# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 分类
class SeventeenkCategoryItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    parentId = scrapy.Field()
    url = scrapy.Field()
    level = scrapy.Field()
    status = scrapy.Field()
    tag= scrapy.Field()
    pass
# 书
class SeventeenkBookItem(scrapy.Item):
    # define the fields for your item here like:
    categoryId = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    newestChapter = scrapy.Field()
    size = scrapy.Field()
    author = scrapy.Field()
    updateTime = scrapy.Field()
    status = scrapy.Field()
    tag= scrapy.Field()
    pass
# 章节
class SeventeenkChapterItem(scrapy.Item):
    # define the fields for your item here like:
    bookId = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    status = scrapy.Field()
    tag= scrapy.Field()
    pass
