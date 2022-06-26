# -*- coding: utf-8 -*-
import re

from w3lib.html import remove_tags, replace_entities
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Identity, TakeFirst


default_input_processor = MapCompose(remove_tags, replace_entities, str.strip)


class DropEmpty:
    def __call__(self, vals):
        return [v for v in vals if v]

class StripCarriage:
    def __call__(self, val):
        val = re.sub(r'\r\n', '', val)
        val = re.sub(' {2,}', ' ', val)
        return val.rstrip()

class ToInt:
    def __call__(self, val):
        if not val:
            return None
        digits = ''.join(re.findall('\\d', val))
        if not digits:
            return None
        return int(digits)


default_output_processor = Compose(DropEmpty(), ' '.join)


class FarnellItem(scrapy.Item):
    url = scrapy.Field()
    #brand = scrapy.Field()
    title = scrapy.Field()
    unit_price = scrapy.Field()
    stock_count = scrapy.Field()
    overview = scrapy.Field()
    information = scrapy.Field()
    manufacturer = scrapy.Field()
    manufacturer_part = scrapy.Field()
    tariff_number = scrapy.Field()
    origin_country = scrapy.Field()
    files = scrapy.Field()
    file_urls = scrapy.Field()
    image_urls = scrapy.Field()
    primary_image_url = scrapy.Field()
    associated_parts = scrapy.Field()
    trail = scrapy.Field()


class FarnellItemLoader(ItemLoader):
    default_item_class = FarnellItem
    default_input_processor = default_input_processor
    default_output_processor = default_output_processor

    def title_out(self, v):
        return re.sub(' \| .*$', '', v[0])

    unit_price_in = Compose(default_input_processor, TakeFirst())
    unit_price_out = Compose(default_output_processor, ToInt())
    stock_count_in = Compose(default_input_processor, TakeFirst())
    stock_count_out = Compose(default_output_processor, ToInt())
    overview_out = Compose(default_output_processor, StripCarriage())
    information_in = Identity()
    information_out = Identity()
    files_out = DropEmpty()
    file_urls_out = DropEmpty()
    image_urls_out = DropEmpty()
    associated_parts_out = Identity()
    trail_out = DropEmpty()
