from scrapy.spider import BaseSpider
from scrapy.selector import Selector
#from scrapy.selector import HtmlXPathSelector
from scrapy import log
from scrapy.http import Request
from scrapy.http import FormRequest
from ompa.items import OmpaItem

# scrapy crawl ompaspider -o items.json -t json
# scrapy crawl ompaspider -a lowage="0" -a highage="6" -a sex="W" -a StrkDist="10025" -o items.json -t json
# scrapy shell http://crgwebservices.com/OMPA/tt-srch.cgi
# sel.xpath("//td")
# sel.xpath("//td[4]/text()")

from scrapy.utils.response import open_in_browser
#  open_in_browser(response)


class MySpider(BaseSpider):
    name = "ompaspider"
    # start_urls = ["http://crgwebservices.com/OMPA/tt-srch.cgi"]
    start_urls = ["http://crgwebservices.com/Springbrook/tt-srch.cgi"]
    # start_urls = ["http://crgwebservices.com/DCSL/tt-srch.cgi"]
    
    def parse(self, response):
        return [FormRequest.from_response(response,formname="TTForm",
                    formdata={"Ctype":"A", "Req_Team":"", "AgeGrp":"", 
                    "lowage": self.lowage, "highage": self.highage, "sex": self.sex, "StrkDist": self.StrkDist, 
                    "How_Many": "25", "foolOldPerl": ""}
                    ,callback=self.parse1,dont_click=True)]
    
    def parse1(self, response):       
        
        hxs = Selector(response)
        rows = hxs.xpath(".//tr")
        items = []
        
        for rows in rows[4:29]:
            item = OmpaItem()
            item["names"] = rows.xpath(".//td[2]/text()").extract()
            item["age"] = rows.xpath(".//td[3]/text()").extract()
            item["time"] = rows.xpath(".//td[4]/text()").extract()
            item["team"] = rows.xpath(".//td[6]/text()").extract()
            items.append(item)           
        return items

        