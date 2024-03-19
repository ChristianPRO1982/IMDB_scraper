import scrapy
import random
import time
from a_my_imdb.items import MovieItem


# headers communs
common_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'fr',
}


class MyImdbSpider(scrapy.Spider):
    name = "my_imdb"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=common_headers)

    def parse(self, response):
        movies = response.css('li.ipc-metadata-list-summary-item')

        ##############
        ##############
        ##############
        movie_max = 1
        ##############
        ##############
        ##############
        i = 0
        for movie in movies:
            i += 1

            # Générer un délai aléatoire entre 1 et 3 secondes
            delay = random.uniform(1, 2)
            time.sleep(delay)

            movie_url = movie.css('a').attrib['href']
            # ou
            # movie_url = movie.css('a ::attr(href)').get()
            yield response.follow(movie_url, callback=self.parse_movie_page, headers=common_headers, cb_kwargs={'movie_rank': i})
            
            if i >= movie_max and movie_max > 0:
                break
    
    def parse_movie_page(self, response, movie_rank):
        movie = response.css('section.ipc-page-section')

        # Titre
        try:
            title = movie.css('h1 span::text').get()
        except:
            title = None
        # Titre original / Public / Durée
        try:
            divs = response.css('div:contains("Titre original")')
            print(">>>len:",len(divs))
            _, orignal_title = divs[-1].xpath('text()').get().strip().split(':')
        except:
            orignal_title = None
        # Année / Public / Durée
        try:
            div = response.xpath('//div[h1]')
            ul = div.css('ul')
            lis = ul.css('li')
            year = lis[0].xpath('string()').get()
            audience = lis[1].xpath('string()').get()
            duration = lis[2].xpath('string()').get()
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
        # Genre
        try:
            genre = response.css('div.ipc-chip-list__scroller span::text').get()
        except:
            genre = None
        # Descriptions(synopsis)
        try:
            plot = response.css('span[data-testid="plot-xl"]::text').get()
        except:
            plot = None
        # Réalisteurs / Scénaristes / Acteurs(Casting principal)
        # Réalisteurs
        try:
            li = response.css('li:contains("Réalisation")')
            uls = li.css('ul')
            lis = uls[0].css('li')
            scrapy_directors = []
            for li in lis:
                scrapy_directors.append(li.css('a::text').get())
        except:
            scrapy_directors = None
        # Scénaristes
        try:
            li = response.css('li:contains("Scénario")')
            uls = li.css('ul')
            lis = uls[0].css('li')
            scrapy_writers = []
            for li in lis:
                scrapy_writers.append(li.css('a::text').get())
        except:
            scrapy_writers = None
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

        
        movie_item = MovieItem()
        movie_item['url'] = response.url
        movie_item['movie_rank'] = movie_rank
        movie_item['title'] = title
        movie_item['orignal_title'] = orignal_title
        movie_item['score'] = score
        movie_item['genre'] = genre
        movie_item['year'] = year
        movie_item['duration'] = duration
        movie_item['plot'] = plot
        movie_item['scrapy_directors'] = scrapy_directors
        movie_item['scrapy_writers'] = scrapy_writers
        movie_item['scrapy_stars'] = scrapy_stars
        movie_item['audience'] = audience
        movie_item['country'] = country
        movie_item['original_language'] = original_language

        yield movie_item
