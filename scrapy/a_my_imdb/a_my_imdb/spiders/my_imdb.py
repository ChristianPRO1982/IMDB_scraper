import scrapy


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

        for movie in movies:
            movie_url = movie.css('a').attrib['href']
            # ou
            # movie_url = movie.css('a ::attr(href)').get()
            yield response.follow(movie_url, callback=self.parse_movie_page, headers=common_headers)
            break
    
    def parse_movie_page(self, response):
        movie = response.css('section.ipc-page-section')

        # Titre
        title = movie.css('h1 span::text').get()
        # Titre original / Public / Durée
        divs = response.css('div:contains("Titre original")')
        _, orignal_title = divs[-1].xpath('text()').get().strip().split(':')
        # Année / Public / Durée
        div = response.xpath('//div[h1]')
        ul = div.css('ul')
        lis = ul.css('li')
        year = lis[0].xpath('string()').get()
        audience = lis[1].xpath('string()').get()
        duration = lis[2].xpath('string()').get()
        # Score
        div = response.css('div[data-testid="hero-rating-bar__aggregate-rating__score"]')
        spans = div[0].css('span')
        score = spans[0].css('::text').get()
        score = float(score.replace(',', '.'))
        # Genre
        genre = response.css('div.ipc-chip-list__scroller span::text').get()
        # Descriptions(synopsis)
        plot = response.css('span[data-testid="plot-xl"]::text').get()
        # Réalisteurs / Scénaristes / Acteurs(Casting principal)
        li = response.css('li:contains("Réalisation")')
        uls = li.css('ul')
        lis = uls[0].css('li')
        directors = []
        for li in lis:
            directors.append(li.css('a::text').get())
        # Scénaristes
        writers = 'writers'
        # Acteurs(Casting principal)
        stars = 'stars'
        # Pays
        country = 'country'
        # Langue d’origine
        original_language = 'original_language'

        yield {
            'url' : response.url,
            'title' : title,
            'orignal_title': orignal_title,
            'score' : score,
            'genre' : genre,
            'year' : year,
            'duration' : duration,
            'plot' : plot,
            'directors' : directors,
            'writers' : writers,
            'stars' : stars,
            'audience' : audience,
            'country' : country,
            'original_language' : original_language,
        }
