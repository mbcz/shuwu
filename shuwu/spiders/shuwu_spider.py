import scrapy
from shuwu.items import ShuwuItem


class ShuwuSpider(scrapy.Spider):

    name = 'shuwu'
    start_urls = ['http://www.shuwu.mobi/page/1']

    def parse(self, response):
        for single in response.xpath('//*[@id="primary"]/ul//div[@class="content "]/h2/a'):
            yield {
                'title': single.xpath('.//text()').extract_first(),
                'url': single.xpath('./@href').extract_first(),
            }
        # for i in range(1, 865):
        current_page = response.xpath(
            '//*[@id="primary"]//span[@class="current"]//text()').extract_first()
        if int(current_page) < 866:
            next_page_url = 'http://www.shuwu.mobi/page/{}'.format(
                int(current_page)+1)
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
