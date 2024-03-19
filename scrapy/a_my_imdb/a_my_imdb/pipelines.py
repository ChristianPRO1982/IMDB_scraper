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
            try:
                value = adapter.get(lowercase_key)
                adapter[lowercase_key] = value.lower()
            except:
                pass
        
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
        
        # Genres / Réalisteurs / Scénaristes / Acteurs(Casting principal)
        # on transforme la liste en un string avec "|"
        fields = ['scrapy_genres', 'scrapy_directors', 'scrapy_writers', 'scrapy_stars']
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
        print()
        print(">>>>>>>>>>>INIT<<<<<<<<<<<<<<<")
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
        print(">>>>>>>>>>>INSERT<<<<<<<<<<<<<<<")
        try:
            self.cur.execute("""
                                INSERT INTO movies250 (url, movie_rank, title, orignal_title, score,
                                                    scrapy_genres, year, duration, plot, scrapy_directors,
                                                    scrapy_writers, scrapy_stars, audience, country, original_language)
                                            VALUES (%s, %s, %s, %s, %s,
                                                    %s, %s, %s, %s, %s,
                                                    %s, %s, %s, %s, %s)
                                """,
                                (item['url'],item['movie_rank'],item['title'],item['orignal_title'],item['score'],
                                item['scrapy_genres'],item['year'],item['duration'],item['plot'],item['scrapy_directors'],
                                item['scrapy_writers'],item['scrapy_stars'],item['audience'],item['country'],item['original_language']))
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