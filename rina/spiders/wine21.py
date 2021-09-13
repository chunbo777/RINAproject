import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import sys
sys.path.insert(0,"/home/tf-dev-01/workspace_sol/wn/rina/rina/")
from items import RinaItem
from bs4 import BeautifulSoup
import traceback
import re

class WineSpider(scrapy.Spider):
    name = "rinawine"
    allowed_domains = ["https://www.wine21.com"]
    # wine_idx=168855
    start_urls=[f"https://www.wine21.com/13_search/wine_view.html?Idx={168855-i}&lq=LIST" for i in range(24000)]
    handle_httpstatus_list = [401, 404]
    download_delay = 1.5
    rules = (
        Rule(LinkExtractor(allow=(r'/recipes/[0-9]+',), deny=(r'/recipes/[0-9]+/')), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=(r'/recipes/[0-9]+',), deny=(r'/recipes/[0-9]+/')), callback='parse_item', follow=True, process_links='process_link', process_request='process_req'),
        # Rule(LinkExtractor(), follow=True)# 디버그 용
    )

    # def start_requests(self):
    #     # recipe_idx = 1
    #     urls = [f"https://www.wine21.com/13_search/wine_view.html?Idx={WineSpider.wine_idx}&lq=LIST"
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
        

    def parse(self, response, **kwargs):
        try :  
            item=RinaItem()
            soup=BeautifulSoup(response.text, "html.parser")

            png = soup.select_one("div.swiper-slide>img").attrs['src']
            
            # try: 
            #     png=p["src"]
            # except:
            #     png="사진정보없음"
            label2 = soup.select_one("#detail > div > div > dl:nth-child(1) > dd > a").text #생산자
            name_ko = soup.select_one('body > section > div.inner > div.clear > div.wine-top-right > dl > dt' ).text
            name_en = soup.select_one('body > section > div.inner > div.clear > div.wine-top-right > dl > dd').text
            classes = soup.select_one("body > section > div.inner > div.clear > div.wine-top-right > div.bagde-box > p > span").text
            price = soup.select_one('body > section > div.inner > div.clear > div.wine-top-right > p.wine-price > strong').text
            # score_expert =soup.select_one("body > section > div.inner > div.clear > div.wine-top-right > p.wine-price > strong").text
            try:
                winery = soup.select_one("#detail > div > div > dl:nth-of-type(2) > dd > a:nth-of-type(2)").text #생산지역
            except:
                winery="생산지역미상"
            # score_customer = soup.select('body > section > div.inner > div.clear > div.wine-top-right > div.wine-top-right-inner > div.score > div > dl:nth-child(2) > dd > span')
            sw = str(soup.select_one("body > section > div.inner > div.clear > div.wine-top-right > div.wine-components > ul > li:nth-child(1) > div"))
            sweet=len(sw.split('=')[3:])
            ac = str(soup.select_one("body > section > div.inner > div.clear > div.wine-top-right > div.wine-components > ul > li:nth-child(2) > div"))
            acidity=len(ac.split('=')[3:])
            # 바디감 가져오기
            bd =  str(soup.select_one("body > section > div.inner > div.clear > div.wine-top-right > div.wine-components > ul > li:nth-child(2) > div"))
            body=len(bd.split('=')[3:])
            tn= str(soup.select_one("body > section > div.inner > div.clear > div.wine-top-right > div.wine-components > ul > li:nth-child(4) > div"))
            tanin = len(tn.split('=')[3:])
            text= soup.select_one('body > section > div.inner > div.clear > div.wine-top-right > div.wine-top-right-inner ').text
            food_match=re.split("\n+",text)
            try:
                i=food_match.index("음식매칭")
                j=food_match.index("전문가 평점 보기")
                food_matching=food_match[i+1:j]
            except:
                food_matching= "추천 정보 없음"
            grape=soup.select_one("#detail > div > div > dl:nth-of-type(3) > dd > a").text
            ain = len(soup.select("#detail > div > div > dl > dd"))
            try:
                for i in range(ain):
                    f = soup.select_one(f"#detail > div > div > dl:nth-of-type({ain-i}) > dt").text
                    if f == "알코올":
                        alcohol = soup.select_one(f"#detail > div > div > dl:nth-of-type({ain-i}) > dd").text
                        break
                    else:
                        alcohol = "알콜정보없음"
            except:
                alcohol = "알콜정보없음"
            # alcohol=soup.select_one(f"#detail > div > div > dl:nth-child(6) > dd").text
            
            raw= soup.select_one("body > section > div.inner > div.clear > div.wine-top-right > p.wine-price" )
            # link = response.url
            raw=str(raw)
            vin =raw.split("(")[1]
            vintage=vin[1:5]
            # vintage_num=r.search(raw)

            item["png"] = png
            item["label2"] = label2
            item["name_ko"] = name_ko
            item["name_en"] =name_en
            item["classes"] = classes
            item["price"] = price
            # item["score_expert"] = score_expert
            item["winery"] = winery
            # item["score_customer"] = score_customer 
            item["sweet"] = sweet
            item["acidity"] = acidity
            item["body"] = body
            item["tanin"] = tanin
            item["food_matching"] = food_matching
            item["grape"] = grape
            item["alcohol"] = alcohol
            item["vintage"] = vintage

            yield item
        
        except Exception as e:
            traceback.print_exc()

        # WineSpider.wine_idx -= 1
        # next_wine = f"https://www.wine21.com/13_search/wine_view.html?Idx={WineSpider.wine_idx}&lq=LIST"
        # yield response.follow(next_wine, callback= self.parse)