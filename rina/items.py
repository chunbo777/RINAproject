# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RinaItem(scrapy.Item):

    png = scrapy.Field()
    label2 = scrapy.Field()
    name_ko = scrapy.Field()
    name_en = scrapy.Field()
    classes = scrapy.Field()
    price = scrapy.Field()
    # score_expert = scrapy.Field()
    winery = scrapy.Field()
    # score_customer = scrapy.Field()
    sweet = scrapy.Field()
    acidity = scrapy.Field()
    body = scrapy.Field()
    tanin = scrapy.Field()
    food_matching = scrapy.Field()
    grape = scrapy.Field()
    alcohol = scrapy.Field()
    vintage = scrapy.Field()


    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
