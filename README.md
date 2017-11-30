# 17K小说网定向爬虫

#### 免责声明：
> 本项目旨在学习Scrapy爬虫框架和使用Mssqlserver数据库，不可使用于商业和个人其他意图。若使用不当，均由个人承担。

#### 项目简介：
> 借助目前超火的爬虫框架scrapy,使用mssqlserver做持久化
  从分类（三级分类）到书目到章节内容的全解析，完全可以依照抓取的数据来做一个自己的小说网

#### 环境、架构
* ![运行环境](https://gitee.com/uploads/images/2017/1130/130154_798e2bb2_1183118.png "config.png")
* ![开发环境](https://gitee.com/uploads/images/2017/1130/130223_be05580f_1183118.png "version.png")
* ![章节抓取运行截图](https://gitee.com/uploads/images/2017/1130/130242_123cc57b_1183118.png "runCut.png")
#### 相关介绍

> 项目目录
 ![项目目录](https://gitee.com/uploads/images/2017/1130/101734_b231dbe7_1183118.png "projectDirectory.png")

#### 爬取对象
* [主站domain](http://www.17k.com/)
* [分类domain](http://all.17k.com/lib/book.html)
* [章节domain](http://www.17k.com/list/2724746.html)

#### 采用技术
> 采用技术：mssql,scrapy

#### 使用步骤
1.根据项目文件下/src/db.sql sql脚本，建立相关数据库表,
2.进入主项目目录，开启命令行 键入 
* scrapy crawl category(一级和二级分类)
* scrapy crawl category_third（三级分类）
* scrapy crawl book（书目）
* scrapy crawl chapter（章节内容）