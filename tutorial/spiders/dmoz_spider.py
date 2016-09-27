from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        sel = Selector(response)
        # #category = sel.xpath('//*[@id="site-list-content"]').extract()
        # category = sel.xpath('//div[@class="site-title"]/text()').extract()
        # for book in category:
        #     #name=book.xpath('//div[@class="site-item "]/div[@class="title-and-desc"]/div[@class="site-title"]').extract()
        #     #name=book.xpath('//div[@class="site-title"]').extract()
        #     print book
        #
        books=sel.xpath('//*[@id="site-list-content"]/*[@class="site-item "]/*[@class="title-and-desc"]')
        items = []
        for book in books:
            link=book.xpath('a/@href').extract()
            title=book.xpath('a/*[@class="site-title"]/text()').extract()
            desc=book.xpath('div[@class="site-descr "]/text()').extract()
            print title,link,desc
            item = DmozItem()
            item['title'] = title
            item['link'] = link
            item['desc'] = desc
            items.append(item)
        return items
        # sites = sel.xpath('//ul/li')
        # for site in sites:
        #     title = site.xpath('a/text()').extract()
        #     link = site.xpath('a/@href').extract()
        #     desc = site.xpath('text()').extract()
        #     print title
