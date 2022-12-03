import scrapy


class BuscaCotaSpider(scrapy.Spider):
    name = 'busca_cota'

    start_urls = ['https://br.investing.com/currencies/usd-brl']

    def parse(self, response):
        for val in response.css('.mobileAndTablet\:py-3+ div'):

            yield{

                'cotacao': val.css('.font-bold .text-2xl::text').get()

            }

        pass
