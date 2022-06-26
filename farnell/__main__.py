from scrapy.crawler import CrawlerProcess

from farnell.spiders.uk_farnell_com import UkFarnellComSpider

if __name__ == '__main__':
    process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(UkFarnellComSpider)
process.start() # the script will block here until the crawling is finished