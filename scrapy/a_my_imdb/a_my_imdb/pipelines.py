# 3 pipelines
# -1 : AMyImdbPipeline : pour nettoyer films et séries
# -2 : SaveToMySQLPipeline : envoi vers la BDD des films
# -3 : SaveToMySQLPipelineTVShow : envoi vers la BDD des films

from itemadapter import ItemAdapter
import mysql.connector
import re


class AMyImdbPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            value = adapter.get(field_name)
            if isinstance(value, list):
                adapter[field_name] = [val.strip() for val in value]
            elif isinstance(value, str):
                adapter[field_name] = value.strip()
        
        # lowercase
        lowercase_keys = ['genre', 'audience']
        for lowercase_key in lowercase_keys:
            try:
                value = adapter.get(lowercase_key)
                adapter[lowercase_key] = value.lower()
            except:
                pass
        
        # budget, gross_worldwide
        budgets = ['budget', 'gross_worldwide']
        try:
            for budget in budgets:
                try:
                    value = adapter.get(budget)
                    value = re.search(r'\b(\d[\d ]*)\b', value)
                    value = value.group(1)
                    value = value.replace('\u202F', '') # Remplacer les espaces insécables (Unicode U+202F) par des espaces normaux
                    adapter[budget] = value
                except:
                    adapter[budget] = 'NULL'
        except:
            pass
        
        # numérical features hors "durée" et  box office
        numericalsfeatures = ['score']
        for numericalfeature in numericalsfeatures:
            value = adapter.get(numericalfeature)
            if ',' in value:
                adapter[numericalfeature] = float(value.replace(',', '.'))
            else:
                adapter[numericalfeature] = float(value)
        
        # durée
        try:
            duration = adapter.get('duration')
            if "h" in duration or "min" in duration:
                try:
                    hours, minutes = duration.split('h ')
                except:
                    hours = 0
                    minutes = duration
                adapter['duration'] = int(hours) * 60 + int(minutes.replace('min', ''))
            else:
                adapter['duration'] = 0
        except:
            adapter['duration'] = 0
        
        # Genres / Réalisteurs / Scénaristes / Acteurs(Casting principal)
        # on transforme la liste en un string avec "|"
        fields = ['scrapy_genres', 'scrapy_directors', 'scrapy_writers', 'scrapy_stars', 'scrapy_creators']
        for field in fields:
            try:
                values = adapter.get(field)
                value_str = ''
                pipe = ''
                for value in values:
                    value_str += pipe + value
                    pipe = '|'
                adapter[field] = value_str
            except:
                pass
        
        # year_stop
        try:
            year_stop = adapter.get('year_stop')
            if year_stop.strip() == '':
                adapter['year_stop'] = 'NULL'
        except:
            pass
        
        # gestion des des "'" et des NULL
        fields_text = ['url', 'title', 'orignal_title', 'scrapy_genres', 'plot',
                       'scrapy_directors', 'scrapy_writers', 'scrapy_creators', 'scrapy_stars', 'audience',
                       'country', 'original_language', 'budget', 'gross_worldwide']
        for field_text in fields_text:
            try:
                value = adapter.get(field_text)
                if field_text == 'audience':
                    if value is None:
                        adapter[field_text] = '"NULL"'
                if value != 'NULL':
                    adapter[field_text] = '"' + value.replace('"', "''") + '"'
                
            except:
                pass

        return item


class SaveToMySQLPipeline:
    
    def __init__(self):
        # connexion à la BDD
        print()
        print(">>>>>>>>>>>INIT MOVIES<<<<<<<<<<<<<<<")
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azertyuiop',
            database = 'my_imdb'
        )

        self.cur = self.conn.cursor()

        # self.cur.execute("DELETE FROM movies250;")
        # self.conn.commit()
        

    def process_item(self, item, spider):
        print()
        print(">>>>>>>>>>>INSERT MOVIE<<<<<<<<<<<<<<<")
        try:
            url,movie_rank,title,orignal_title,score = item['url'],item['movie_rank'],item['title'],item['orignal_title'],item['score']
            scrapy_genres,year,duration,plot,scrapy_directors = item['scrapy_genres'],item['year'],item['duration'],item['plot'],item['scrapy_directors']
            scrapy_writers,scrapy_stars,audience,country,original_language = item['scrapy_writers'],item['scrapy_stars'],item['audience'],item['country'],item['original_language']
            budget,gross_worldwide = item['budget'],item['gross_worldwide']
            
            # on insert les données dans une seule table "movies250"
            # des champs tampons commence par "scrapy_"
            # les valeurs hydrateront les autres tables par le trigger d'INSERT
            request = f"""
INSERT INTO movies250 (url, movie_rank, title, orignal_title, score,
                    scrapy_genres, year, duration, plot, scrapy_directors,
                    scrapy_writers, scrapy_stars, audience, country, original_language,
                    budget, gross_worldwide)
            VALUES ({url}, {movie_rank}, {title}, {orignal_title}, {score},
                    {scrapy_genres}, {year}, {duration}, {plot}, {scrapy_directors},
                    {scrapy_writers}, {scrapy_stars}, {audience}, {country}, {original_language},
                    {budget}, {gross_worldwide})
"""
            
            print("request=",request)
            self.cur.execute(request)
        except Exception as e:
            print(e)
            print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
            print('"' + item['title'] + '" est déjà en base [' + item['url'] + '].')
            print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
            print()
        
        self.conn.commit()
        return item
    

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


class SaveToMySQLPipelineTVShow:
    
    def __init__(self):
        print()
        print(">>>>>>>>>>>INIT TV SHOWS<<<<<<<<<<<<<<<")
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azertyuiop',
            database = 'my_imdb'
        )

        self.cur = self.conn.cursor()

        # self.cur.execute("DELETE FROM tv_shows250;")
        # self.conn.commit()
        

    def process_item(self, item, spider):
        print()
        print(">>>>>>>>>>>INSERT TV SHOW<<<<<<<<<<<<<<<")
        try:
            url,tvshow_rank,title,orignal_title,score = item['url'],item['tvshow_rank'],item['title'],item['orignal_title'],item['score']
            scrapy_genres,year_start,year_stop,duration,plot = item['scrapy_genres'],item['year_start'],item['year_stop'],item['duration'],item['plot']
            scrapy_creators,scrapy_stars,audience,country,original_language = item['scrapy_creators'],item['scrapy_stars'],item['audience'],item['country'],item['original_language']

            request = f"""
INSERT INTO tv_shows250 (url, tvshow_rank, title, orignal_title, score,
                    scrapy_genres, year_start, year_stop, duration, plot,
                    scrapy_creators, scrapy_stars, audience, country, original_language)
            VALUES ({url}, {tvshow_rank}, {title}, {orignal_title}, {score},
                    {scrapy_genres}, {year_start}, {year_stop}, {duration}, {plot},
                    {scrapy_creators}, {scrapy_stars}, {audience}, {country}, {original_language})
"""
            print("request=",request)
            self.cur.execute(request)
        except Exception as e:
            print(e)
            print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
            print('"' + item['title'] + '" est déjà en base [' + item['url'] + '].')
            print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
            print()
        
        self.conn.commit()
        return item
    

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()