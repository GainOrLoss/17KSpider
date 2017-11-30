# -*- coding: utf-8 -*-
import scrapy

from SeventeenK.items import SeventeenkCategoryItem
from SeventeenK.mssql import mssql_helper
class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['www.17k.com']
    start_urls = ['http://all.17k.com/lib/book.html']
    ms=mssql_helper()
    # 一级和二级分类
    def parse(self, response):
        selectors=response.xpath("//*[@class='allzplb']")
        for selector in selectors:
            if selectors.index(selector)>=2:
                sel_first=selector.xpath("./a[1]")
                item=SeventeenkCategoryItem()
                item["name"]=sel_first.xpath("./span/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                item["parentId"]=0
                item["url"]="http://all.17k.com{}".format(sel_first.xpath("./@href").extract()[0].encode('utf-8').decode('utf-8'))
                item["level"]=1
                item["status"]=0
                item["tag"]=0
                yield item
                pid=self.ms.execute_query("select Id from [17K_Category] where Name='{}'".format(item["name"]))[0][0]
                sel_seconds=selector.xpath("./a")
                for sel_second in sel_seconds:
                    if sel_seconds.index(sel_second)>=1:
                        item_second=SeventeenkCategoryItem()
                        item_second["name"]=sel_second.xpath("./text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                        item_second["parentId"]=pid
                        item_second["url"]="http://all.17k.com{}".format(sel_second.xpath("./@href").extract()[0].encode('utf-8').decode('utf-8'))
                        item_second["level"]=2
                        item_second["status"]=0
                        item["tag"]=0
                        yield item_second
                        pass
                    pass
                pass
            pass
        pass
       
