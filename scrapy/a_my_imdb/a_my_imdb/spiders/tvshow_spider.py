import scrapy
import random
import time
from a_my_imdb.items import TVShowItem


# headers communs
common_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'fr',
}

class TvshowSpiderSpider(scrapy.Spider):
    name = "tvshow_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=common_headers)

    def parse(self, response):
        tvshows = response.css('li.ipc-metadata-list-summary-item')

        ##############
        ##############
        ##############
        tvshow_max = 10
        ##############
        ##############
        ##############
        i = 0
        for tvshow in tvshows:
            i += 1

            # Générer un délai aléatoire entre 1 et 3 secondes
            delay = random.uniform(1, 2)
            time.sleep(delay)

            tvshow_url = tvshow.css('a').attrib['href']
            # ou
            # tvshow_url = tvshow.css('a ::attr(href)').get()
            yield response.follow(tvshow_url, callback=self.parse_tvshow_page, headers=common_headers, cb_kwargs={'tvshow_rank': i})
            
            if i >= tvshow_max and tvshow_max > 0:
                break
    
    def parse_tvshow_page(self, response, tvshow_rank):
        tvshow = response.css('section.ipc-page-section')
        
        # Titre
        try:
            title = tvshow.css('h1 span::text').get()
        except:
            title = None
        # Titre original / Public / Durée
        try:
            divs = response.css('div:contains("Titre original")')
            _, orignal_title = divs[-1].xpath('text()').get().strip().split(':')
        except:
            orignal_title = None
        # Année / Public / Durée
        try:
            div = response.xpath('//div[h1]')
            ul = div.css('ul')
            lis = ul.css('li')
            year = lis[1].xpath('string()').get()
            year_start, year_stop = year.strip().split('–')
            audience = lis[2].xpath('string()').get()
            duration = lis[3].xpath('string()').get()
        except:
            year = None
            audience = None
            duration = None
        # Score
        try:
            div = response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"]')
            spans = div[0].css('span')
            score = spans[0].css('::text').get()
        except:
            score = None
        # Genres
        try:
            # genre = response.css('div.ipc-chip-list__scroller span::text').get()
            genres = response.css('div.ipc-chip-list__scroller span')
            scrapy_genres = []
            for genre in genres:
                scrapy_genres.append(genre.css('span::text').get())
        except:
            genre = None
        # Descriptions(synopsis)
        try:
            plot = response.css('span[data-testid="plot-xl"]::text').get()
        except:
            plot = None
        # Créateurs / Acteurs(Casting principal)
        # Créateurs
        try:
            li = response.css('li:contains("Création")')
            uls = li.css('ul')
            lis = uls[0].css('li')
            scrapy_creators = []
            for li in lis:
                scrapy_creators.append(li.css('a::text').get())
        except:
            scrapy_creators = None
        # Acteurs(Casting principal)
        try:
            li = response.css('li:contains("Casting principal")')
            uls = li.css('ul')
            lis = uls[0].css('li')
            scrapy_stars = []
            for li in lis:
                scrapy_stars.append(li.css('a::text').get())
        except:
            scrapy_stars = None
        # Pays
        try:
            li = response.css('li:contains("Pays d’origine")')
            lis = li.css('div ul li')
            li = lis[0]
            country = li.css('a::text').get()
        except:
            country = None
        # Langue d’origine
        try:
            li = response.css('li:contains("Langue")')
            lis = li.css('div ul li')
            li = lis[0]
            original_language = li.css('a::text').get()
        except:
            original_language = None

        
        tvshow_item = TVShowItem()
        tvshow_item['url'] = response.url
        tvshow_item['tvshow_rank'] = tvshow_rank
        tvshow_item['title'] = title
        tvshow_item['orignal_title'] = orignal_title
        tvshow_item['score'] = score
        tvshow_item['scrapy_genres'] = scrapy_genres
        tvshow_item['year_start'] = year_start
        tvshow_item['year_stop'] = year_stop
        tvshow_item['duration'] = duration
        tvshow_item['plot'] = plot
        tvshow_item['scrapy_creators'] = scrapy_creators
        tvshow_item['scrapy_stars'] = scrapy_stars
        tvshow_item['audience'] = audience
        tvshow_item['country'] = country
        tvshow_item['original_language'] = original_language

        yield tvshow_item

