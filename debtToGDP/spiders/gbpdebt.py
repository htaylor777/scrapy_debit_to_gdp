import scrapy
import csv
import os
import json
import requests
import pandas as pd
import logging

names = []
pcs = []
populations = []

class GbpdebtSpider(scrapy.Spider):
    name = 'gbpdebt'
    #allowed_domains = ['worldpopulationreview.com/countries/countries-by-national-debt']
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        data = response.xpath("//table[@class='jsx-1487038798 table table-striped tp-table-body'][1]/tbody/tr")
      
        for row in data:
            name = row.xpath('.//text()').get()
            pc = row.xpath('.//td[2]/text()').get()
            population = row.xpath('.//td[3]/text()').get()
            yield {
                'Name': name,
                'Percentage': pc,
                'Population': population
            }
            names.append(name)
            pcs.append(pc)
            populations.append(population)
            data = {'Name': names, 'Percentage': pcs, 'Population': populations,}
            df = pd.DataFrame(data=data)
            df.index += 1
            df.to_excel("gdp.xlsx")
