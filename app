import scrapy
from ..items import BookItem
import re
class AppSpider(scrapy.Spider):
    name = "app"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/latest"]

    def parse(self, response):
        #print(response)
        books = response.xpath('//ul[@class="chart-dashed-list"]/li')
        for book in books:
            link = book.xpath('.//h2/a/@href').get()
            #print(link)
            yield scrapy.Request(url=link,callback=self.parse_detail)
        next_url = response.xpath('//*[@id="content"]/div[2]/div[1]/div[4]/span[4]/a/@href').get()
        if next_url is not None:
            next_url = response.urljoin(next_url)
            #print(next_url)
            yield scrapy.Request(url=next_url,callback=self.parse)
        else:
            next_url = response.xpath('//*[@id="content"]/div[2]/div[1]/div[4]/span[3]/a/@href').get()
            next_url = response.urljoin(next_url)
            #print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)



    def parse_detail(self,response):
        item = BookItem()

        info_text = response.xpath('//*[@id="info"]').get()

        item['bookname'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').get()
        item['author'] = response.xpath('//*[@id="info"]/span[1]/a/text()').get()
        item['publisher'] = response.xpath('//*[@id="info"]/a[1]/text()').get()
        item['producer'] = response.xpath('//*[@id="info"]/a[2]/text()').get()
        #- 使用text()[n]索引定位文本 是非常不可靠的，因为：

        '''- 不同书籍页面的信息结构可能不同
        - 豆瓣页面的布局可能会变化
        - 文本节点的索引位置在不同页面中不一致
        - 3.
        建议改进方法 ：使用更稳定的方式解析豆瓣图书信息，比如通过信息标签进行定位：'''
        #可以用re
        '''//*[@id="info"]/text()[2]''//*[@id="info"]/text()[2]''//*[@id="info"]/text()[2]
        item['original_title'] = response.xpath('//*[@id="info"]/text()[2]').get()
        item['translation_name'] = response.xpath('//*[@id="info"]/span[5]/a/text()').get()
        item['publication_year'] = response.xpath('//*[@id="info"]/text()[3]').get()
        item['page_number'] = response.xpath('//*[@id="info"]/text()[4]').get()
        #item['price'] = response.xpath('//*[@id="info"]/text()[5]').get()
        price_match = re.search(r'定价:</span>\s*(\d+\.?\d*)元', info_text)

        item['price'] = price_match.group(1) if price_match else ''
        item['binding'] = response.xpath('//*[@id="info"]/text()[6]').get()
        item['isbn'] = response.xpath('//*[@id="info"]/text()[7]').get()'''

        yield item



