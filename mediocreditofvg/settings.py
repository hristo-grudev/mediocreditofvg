BOT_NAME = 'mediocreditofvg'

SPIDER_MODULES = ['mediocreditofvg.spiders']
NEWSPIDER_MODULE = 'mediocreditofvg.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'mediocreditofvg.pipelines.MediocreditofvgPipeline': 100,

}