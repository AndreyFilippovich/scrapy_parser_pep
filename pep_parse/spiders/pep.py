import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_links = response.css(
            '#numerical-index tbody > tr > td > a::attr(href)'
        )
        for link in all_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        text = response.css('article h1::text').get()
        t1, number, t3, name = text.split(' ', 3)
        data = {
            'number': number,
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
