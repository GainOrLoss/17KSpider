# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from SeventeenK.mssql import mssql_helper

class SeventeenkPipeline(object):
    def __init__(self):
        self.ms=mssql_helper()
        pass
    def process_item(self, item, spider):
        strSql=""
        if item["tag"]==0:
            strSql="insert into [17K_Category](Name,ParentId,Url,Level,Status) values('{0}','{1}','{2}','{3}','{4}')".format(item["name"],item["parentId"],item["url"],item["level"],item["status"])
            pass
        elif item["tag"]==1:
            strSql="insert into [17K_Book]([CategoryId],Name,[NewestChapter],[Size],[Author],[UpdateTime],Status,Url) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(item["categoryId"],item["name"],item["newestChapter"],int(item["size"]),item["author"],item["updateTime"],item["status"],item["url"])
        else:
            strSql="insert into [17K_Chapter]([BookId],Title,[Content],Status) values('{0}','{1}','{2}','{3}')".format(item["bookId"],item["title"],item["content"],item["status"])
       
        print(strSql)
        self.ms.execute_sql(strSql)
        return item
