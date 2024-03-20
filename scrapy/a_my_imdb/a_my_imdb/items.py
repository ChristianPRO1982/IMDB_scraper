# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AMyImdbItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

def serialize_score(value):
    return float(value.replace(',', '.'))

class MovieItem(scrapy.Item):
    url = scrapy.Field()
    movie_rank = scrapy.Field()
    title = scrapy.Field()
    orignal_title = scrapy.Field()
    # score = scrapy.Field(serialize=serialize_score) # à utilisant en dehors d'un pipeline pour aller vite mais c'est mieux dans un pipeline
    score = scrapy.Field(serialize=serialize_score)
    scrapy_genres = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
    plot = scrapy.Field()
    scrapy_directors = scrapy.Field()
    scrapy_writers = scrapy.Field()
    scrapy_stars = scrapy.Field()
    audience = scrapy.Field()
    country = scrapy.Field()
    original_language = scrapy.Field()
    budget = scrapy.Field()
    gross_worldwide = scrapy.Field()

class TVShowItem(scrapy.Item):
    url = scrapy.Field()
    tvshow_rank = scrapy.Field()
    title = scrapy.Field()
    orignal_title = scrapy.Field()
    score = scrapy.Field(serialize=serialize_score)
    scrapy_genres = scrapy.Field()
    year_start = scrapy.Field()
    year_stop = scrapy.Field()
    duration = scrapy.Field()
    plot = scrapy.Field()
    scrapy_creators = scrapy.Field()
    scrapy_stars = scrapy.Field()
    audience = scrapy.Field()
    country = scrapy.Field()
    original_language = scrapy.Field()