# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class OmpaItem(Item):
    # define the fields for your item here like:
    names = Field()
    age = Field()
    time = Field()
    team = Field()
    # date = Field()
    pass
