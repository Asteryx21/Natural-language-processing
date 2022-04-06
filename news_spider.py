import os.path
import scrapy
save_path = 'C:/Users/evans/OneDrive/Desktop/Language_Technology/html_pages'
class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [ 'https://www.theverge.com/film/archives',
    'https://www.theverge.com/environment/archives','https://www.theverge.com/space/archives',
    'https://www.theverge.com/health/archives', 'https://www.theverge.com/books/archives']

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'article-%s.html' %page
        complete_name = os.path.join(save_path, filename)
        with open(complete_name, 'wb') as f:
            f.write(response.body)
        
        a_selectors = response.css('h2.c-entry-box--compact__title > a').xpath('@href').extract()
        #loop through articles
        for selector in a_selectors:
            request = response.follow(selector,callback=self.parse)
            yield request
        #go on next page
        next_page = response.css('a.c-pagination__next.c-pagination__link.p-button::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback= self.parse)

        