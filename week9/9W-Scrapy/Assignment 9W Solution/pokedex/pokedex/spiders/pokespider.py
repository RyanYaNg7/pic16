# -*- coding: utf-8 -*-
import scrapy


class PokespiderSpider(scrapy.Spider):
    name = 'pokespider'
#    allowed_domains = ['https://pokemondb.net/']
    start_urls = ['https://pokemondb.net/pokedex/national']

    def parse(self, response):
        for pokemon in response.css("span.infocard-tall"):
            texts = pokemon.css("::text").extract()
            name_number =  {"Name": texts[1] , "Number": texts[0][1:]}
            link = pokemon.css("a.pkg::attr(href)").extract_first()
            request = response.follow(link, self.parse2)
            request.meta['name_number'] = name_number
            yield request
            
    def parse2(self, response):
        name_number = response.meta["name_number"]
        name_number["about"] = response.css("div.tabset-basics + div + h2 + table td ::text").extract_first()
        yield name_number