import scrapy

from scrapy.loader import ItemLoader
from ..items import MediocreditofvgItem
from itemloaders.processors import TakeFirst


class MediocreditofvgSpider(scrapy.Spider):
	name = 'mediocreditofvg'
	start_urls = ['https://www.mediocredito.fvg.it/category/avvisi-e-comunicati/']

	def parse(self, response):
		post_links = response.xpath('//a[@class="btn btn-primary pull-right"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="next"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="col-md-9 col-sm-9"]/div/p[position()>1]//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('(//div[@class="col-md-9 col-sm-9"]/div/p)[1]//text()').get()

		item = ItemLoader(item=MediocreditofvgItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
