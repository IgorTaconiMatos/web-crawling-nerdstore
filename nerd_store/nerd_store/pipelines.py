# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class NerdStorePipeline:

	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn = sqlite3.connect('nerdstore_products.db')
		self.cur = self.conn.cursor()

	def create_table(self):
		self.cur.execute("""DROP TABLE IF EXISTS products""")

		sql = """
			CREATE TABLE products(
				name TEXT,
				price INTEGER,
				images TEXT,
				description TEXT,
				specifications TEXT,
				url TEXT UNIQUE
			)
		"""
		self.cur.execute(sql)

	def db_insert(self, item):
		self.cur.execute("""
			INSERT INTO products(name, price, images, description, specifications, url)
				VALUES('{}', '{}', '{}', '{}', '{}', '{}')
			""".format(
			item['name'],
			item['price'],
			item['images'],
			item['description'],
			item['specifications'],
			item['url']
		))
		self.conn.commit()

	def process_item(self, item, spider):
		self.db_insert(item)
		return item
