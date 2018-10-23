#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:09:57 2018

@author: Ryan
"""

import scrapy

class PokeinfoSpider(scrapy.Spider):
    name = "pokeinfo"
    start_urls = ['https://pokemondb.net/pokedex/national']
    
    def parse(self, response):
# =============================================================================
#         for pokemon in response.css("div.infocard-tall-list span.infocard-tall"):
#             yield {
#                     'number': pokemon.css("small::text")[0].extract()[1:4],
#                     'name': pokemon.css("a.ent-name::text").extract(),
#             }
#             
# =============================================================================
#        i = 1
        for pokemon in response.css("span.infocard-tall"):
            a = pokemon.css("a.ent-name")
            url = response.urljoin(a.xpath('@href').extract_first())
            request = scrapy.Request(url, callback=self.parse_each)
            pk_name = a.xpath('text()').extract()
            request.meta['pk_name'] = pk_name
            request.meta['pk_number'] = pokemon.css("small::text")[0].extract()[1:4]
            yield request
# =============================================================================
#             i = i + 1
#             if i == 10:
#                 break
# =============================================================================
            
    
    def parse_each(self, response):
        yield {
            "number": response.meta['pk_number'],
            "name": response.meta['pk_name'],
            "pokedex": response.css("article.main-content>table.vitals-table td::text").extract_first(),
        }
        
