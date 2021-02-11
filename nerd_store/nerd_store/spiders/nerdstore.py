from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import NerdStoreItem


class NerdStoreSpider(CrawlSpider):
	name = 'nerdstore'
	allowed_domains = ['nerdstore.com.br']
	start_urls = ['https://nerdstore.com.br/']

	rules = (
		Rule(
			LinkExtractor(
				restrict_xpaths=('//li[@class="header-desktop__nav__menu__parent"]')
			)
		),
		Rule(
			LinkExtractor(
				restrict_css=('a.page-numbers')
			)
		),
		Rule(
			LinkExtractor(
				restrict_css=('a.woocommerce-LoopProduct-link')
			),
			callback='parse_product'
		)
	)

	def parse_product(self, response):
		items = NerdStoreItem()

		name = response.xpath(
			'//h1[@class="product_title entry-title"]//text()'
		).get()
		price = response.xpath(
			'//bdi/text()'
		).get()
		images = ' - '.join(response.css(
			'.woocommerce-product-gallery__image a::attr(href)'
		).getall())
		description = ' '.join(response.xpath(
			'//div[@class="single-product__description__content"]//p//text()'
		).getall())
		specifications = ' '.join(response.xpath(
			'//div[@class="single-product__description__content"]//ul//li//text()'
		).getall())

		items['name'] = name
		items['price'] = price
		items['images'] = images
		items['description'] = description
		items['specifications'] = specifications
		items['url'] = response.url

		yield items
