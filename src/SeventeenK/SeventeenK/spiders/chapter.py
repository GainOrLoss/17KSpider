# -*- coding: utf-8 -*-
import scrapy

from SeventeenK.mssql import mssql_helper
from SeventeenK.items import SeventeenkChapterItem
class ChapterSpider(scrapy.Spider):
    name = 'chapter'
    allowed_domains = ['www.17k.com']
    start_urls = ['http://www.17k.com']
    ms=mssql_helper()

    def parse(self, response):
        rt=self.ms.execute_query("select Id,Url from [17K_Book]")
        for x in rt:
            id=x[0]
            url=x[1].replace("book","list")
            yield scrapy.Request(url,meta={'id':id},callback=self.parse_chapter)
        pass
    #章节
    def parse_chapter(self, response):
        selectors=response.xpath("//*[@class='Volume']/dd/a")
        book_id=response.meta["id"]
        for selector in selectors:
            item=SeventeenkChapterItem()
            item["bookId"]=book_id
            item["title"]=selector.xpath("./span/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
            item["status"]=0
            url=selector.xpath("./@href").extract()[0].strip().encode('utf-8').decode('utf-8')
            url="{0}{1}".format(self.start_urls[0],url)
            yield scrapy.Request(url,meta=item,callback=self.parse_content)
            pass
        pass

    #章节内容
    def parse_content(self, response):
        item=response.meta
        item["tag"]=2
        item["content"]=response.xpath("//*[@class='p']")[0].xpath("string(.)").extract()[0].strip().encode('utf-8').decode('utf-8')
        yield item
        pass