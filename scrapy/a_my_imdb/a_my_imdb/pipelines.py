# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


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
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()
        
        # numérical features hors "durée"
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
            hours, minutes = duration.split('h ')
            adapter['duration'] = int(hours) * 60 + int(minutes.replace('min', ''))
        except:
            adapter['duration'] = 0
        
        # Réalisteurs / Scénaristes / Acteurs(Casting principal)
        # on transforme la liste en un string avec "|"
        fields = ['scrapy_directors', 'scrapy_writers', 'scrapy_stars']
        for field in fields:
            values = adapter.get(field)
            value_str = ''
            pipe = ''
            for value in values:
                value_str += pipe + value
                pipe = '|'
            adapter[field] = value_str


        return item


class SaveToMySQLPipeline:
    
    def __init__(self):
        print(">>>>>>>>>>>CREATE<<<<<<<<<<<<<<<")
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azertyuiop',
            database = 'my_imdb'
        )

        self.cur = self.conn.cursor()

        self.cur.execute("DELETE FROM movies250;")
        self.conn.commit()

        # self.cur.execute("""
        #                  CREATE TABLE IF NOT EXISTS movies250 (
        #                     url varchar(255) NOT NULL,
        #                     movie_rank SMALLINT NOT NULL,
        #                     title varchar(150) NULL,
        #                     orignal_title VARCHAR(150) NULL,
        #                     score TINYINT NULL,
        #                     genre VARCHAR(50) NULL,
        #                     year SMALLINT NULL,
        #                     duration SMALLINT NULL,
        #                     plot TEXT NULL,
        #                     scrapy_directors TEXT NULL,
        #                     scrapy_writers TEXT NULL,
        #                     scrapy_stars TEXT NULL,
        #                     audience VARCHAR(50) NULL,
        #                     country VARCHAR(50) NULL,
        #                     original_language VARCHAR(50) NULL,
        #                     CONSTRAINT movies250_pk PRIMARY KEY (url)
        #                  )
        #                  """)
        

    def process_item(self, item, spider):
        print(">>>>>>>>>>>INSERT<<<<<<<<<<<<<<<")
        self.cur.execute("""
                            INSERT INTO movies250 (url, movie_rank, title, orignal_title, score,
                                                genre, year, duration, plot, scrapy_directors,
                                                scrapy_writers, scrapy_stars, audience, country, original_language)
                                        VALUES (%s, %s, %s, %s, %s,
                                                %s, %s, %s, %s, %s,
                                                %s, %s, %s, %s, %s)
                            """,
                            (item['url'],item['movie_rank'],item['title'],item['orignal_title'],item['score'],
                            item['genre'],item['year'],item['duration'],item['plot'],item['scrapy_directors'],
                            item['scrapy_writers'],item['scrapy_stars'],item['audience'],item['country'],item['original_language']))
        
        self.conn.commit()
        return item
    

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()