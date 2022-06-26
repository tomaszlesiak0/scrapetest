# -*- coding: utf-8 -*-
import scrapy

from farnell.items import (
    FarnellItemLoader,
    default_input_processor,
    default_output_processor,
)


def process(x):
    return default_output_processor(default_input_processor(x.extract()))


class UkFarnellComSpider(scrapy.Spider):
    name = 'uk.farnell.com'
    allowed_domains = ['uk.farnell.com']
    start_urls = [
        'http://uk.farnell.com/c/electrical/prl/results',
        'http://uk.farnell.com/c/engineering-software/prl/results',
        'http://uk.farnell.com/c/wireless-modules-adaptors/prl/results',
    ]

    def parse(self, response):
        for page in response.css('span.pageLink *::attr(href)'):
            yield response.follow(page)
        items = list(response.css('td.mftrPart *::attr(href)'))
        if len(items) == 25:
            for item in items:
                yield response.follow(item, callback=self.parse_item)
        else:
            self.logger.debug('No more products')

    def parse_item(self, response):
        il = FarnellItemLoader(response=response)
        il.add_value('url', response.url)
        il.add_css('title', 'title')
        il.add_css('unit_price', '.productPrice span')
        il.add_xpath('stock_count', '//td[@class="qty"]')
        il.add_css('overview', '.product-overview .collapsable-content')
        for info_line in response.css('#pdpSection_pdpProdDetails dt'):
            il.add_value('information', {
                'name': process(info_line),
                'value': process(info_line.xpath('./following-sibling::dd[1]'))
            })
        il.add_xpath(
            'manufacturer',
            '//*[@itemprop="http://schema.org/manufacturer"]')
        il.add_xpath(
            'manufacturer_part',
            '//dt[.//text()[contains(.,"Manufacturer Part No")]]/following-sibling::dd')  # noqa
        il.add_xpath(
            'tariff_number',
            '//dt[./text()[contains(.,"Tariff No")]]/following-sibling::dd[1]')  # noqa
        il.add_xpath(
            'origin_country',
            '//dt[./text()[contains(.,"Country of Origin")]]/following-sibling::dd[1]/text()')  # noqa
        il.add_xpath('associated_parts', '//*[contains(@class,"mfrnum")]')
        for file in response.xpath('//div[@class="mainPdpWrapper"]//dd//a[./@href[contains(.,".pdf")]]'):  # noqa
            il.add_value('files', process(file))
            il.add_value('file_urls', file.xpath('@href').extract())
        il.add_css('image_urls', '.slide *::attr(data-full)')
        il.add_css('trail', '#breadcrumb ul a')
        item = il.load_item()
        if item.get('image_urls'):
            item['primary_image_url'] = item['image_urls'].pop(0)
        item['trail'] = item['trail'][1:-1]
        yield item
