# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScrapingMoneyballItem(scrapy.Item):
    # define the fields for your item here like:
    player_name = scrapy.Field()
    player_age = scrapy.Field()
    market_value = scrapy.Field()
    # player_name = scrapy.Field()
    # club = scrapy.Field()
    # player_age = scrapy.Field()
    # position = scrapy.Field()
    # Apps = scrapy.Field()
    # Minutes = scrapy.Field()
    # Goals = scrapy.Field()
    # Assists = scrapy.Field()
    # Yellow_Cards = scrapy.Field()
    # Red_Cards = scrapy.Field()
    # Shots_per_Game = scrapy.Field()
    # Pass_Success_Percentage = scrapy.Field()
    # AerialsWon = scrapy.Field()
    # MotM = scrapy.Field()
    # Rating = scrapy.Field()


