import scrapy
from ..items import WebScrapingMoneyballItem
import pandas as pd


class MoneyballSpiderSpider(scrapy.Spider):
    name = 'moneyball_spider'
    # allowed_domains = ['https://1xbet.whoscored.com/Statistics']
    start_urls = ['https://www.transfermarkt.com/marktwertetop/wertvollstespieler']

    def parse(self, response):
        items = WebScrapingMoneyballItem()

        pl_name = response.css('#yw1 .spielprofil_tooltip').css('::text').extract()
        age = response.css('.odd .zentriert:nth-child(3)').css('::text').extract()
        value = response.css('#yw1 b').css('::text').extract()
        # player_name = response.css('#player-table-statistics-body .iconize-icon-left').css('::text').extract()
        # club_name = response.css('.team-name').css('::text').extract()
        # player_age = response.css('.player-meta-data:nth-child(1)').css('::text').extract()
        # position_played = response.css('.player-meta-data+ .player-meta-data').css('::text').extract()
        # player_appearances = response.css('.grid-ghost-cell+ td').css('::text').extract()
        # minutes_played = response.css('.minsPlayed').css('::text').extract()
        # goals_scored = response.css('#player-table-statistics-body .goal').css('::text').extract()
        # assists_given = response.css('.assistTotal').css('::text').extract()
        # num_yellow_cards = response.css('.yellowCard').css('::text').extract()
        # num_red_cards = response.css('.redCard').css('::text').extract()
        # shots_per_game = response.css('#player-table-statistics-body .shotsPerGame').css('::text').extract()
        # successful_passes = response.css('#player-table-statistics-body .passSuccess').css('::text').extract()
        # aerials_won = response.css('#player-table-statistics-body .aerialWonPerGame').css('::text').extract()
        # man_of_match = response.css('.manOfTheMatch').css('::text').extract()
        # rating = response.css('#player-table-statistics-body .sorted').css('::text').extract()

        items['player_name'] = pl_name
        items['player_age'] = age
        items['market_value'] = value
        # items['player_name'] = player_name
        # items['club'] = club_name
        # items['player_age'] = player_age
        # items['Apps'] = player_appearances
        # items['Minutes'] = minutes_played
        # items['Goals'] = goals_scored
        # items['Assists'] = assists_given
        # items['Yellow_Cards'] = num_yellow_cards
        # items['Red_Cards'] = num_red_cards
        # items['Shots_per_Game'] = shots_per_game
        # items['Pass_Success_Percentage'] = successful_passes
        # items['AerialsWon'] = aerials_won
        # items['MotM'] = man_of_match
        # items['Rating'] = rating
        next_page = response.css('li.naechste-seite a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        yield items







