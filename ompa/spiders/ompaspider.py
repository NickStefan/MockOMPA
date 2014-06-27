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


class MySpider(BaseSpider):
    name = "ompaspider"
    start_urls = ["http://www.acornswim.com",
    "http://www.acornswim.com/Database/index.php?league=ompa",
    "http://www.acornswim.com/Database/search/ttsearch.php?sttchoice=Search+Top+Times"]
    
    def parse(self, response):
        #open_in_browser(response)
        return [FormRequest.from_response(response,formname="ttimes",
                    formdata={"ttteams":"", "ttagegroups":"", 
                    "ttloage": self.ttloage, "tthiage": self.tthiage, "ttgenders": self.ttgenders, "ttdistances": self.ttdistances, 
                    "ttstrokes": self.ttstrokes,"ttdisplay": "50"}
                    ,callback=self.parse1,dont_click=True)]
    
    def parse1(self, response):       
        hxs = Selector(response)
        rows = hxs.xpath(".//tr")
        items = []
        
        for rows in rows[4:39]:
            item = OmpaItem()
            item["names"] = rows.xpath(".//td[3]/a[1]/text()").extract()
            item["age"] = rows.xpath(".//td[4]/text()").extract()
            item["time"] = rows.xpath(".//td[5]/text()").extract()
            item["team"] = rows.xpath(".//td[7]/text()").extract()
            items.append(item)           
        return items

        
