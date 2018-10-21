# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class DoubanItem(Item):
    table = 'movies'
    movie = Field()
    director = Field()
    writer = Field()
    actor = Field()
    types = Field()
    region = Field()
    lang = Field()
    ReleaseDate = Field()
    runtime = Field()
    alias = Field()
    IMDb = Field()
    score = Field()
    vote = Field()
