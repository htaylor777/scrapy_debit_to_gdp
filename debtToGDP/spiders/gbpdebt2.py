import scrapy


class GdpDebt2Spider(scrapy.Spider):
    name = 'gdpdebt2'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            yield {
                'country_name': row.xpath(".//td[1]/a/text()").get(),
                'gdp_debt': row.xpath(".//td[2]/text()").get()
            }

