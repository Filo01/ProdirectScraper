import scrapy
from jinja2 import Template
from ..emailer import send_mail


class PageSpider(scrapy.Spider):
    home_url = 'http://www.prodirectselect.com/'

    def parse(self, response):
        '''
        Will be called to handle the response downloaded for each of the
        requests made.
        :param response:  holds the page content
        :return:
        '''
        collection = []
        for item in response.css('div.list div.item'):
            trainers = {
                'Price ': item.css('p.price::text').extract_first(),
                'Description ': item.css('a::text').extract_first(),
                'More info ': self.home_url +
                              item.css('a::attr(href)').extract_first()
            }
            collection.append(trainers)

        template = Template("""
        <table>
            {% for item in items %}
                 <ul>
                 {% for key, value in item.items() %}
                    {% if value %}
                       <li>{{value}}</li>
                    {% endif %}
                {% endfor %}
                </ul>
            {% endfor %}
        </table>
        """)
        table = template.render(items=collection)
        send_mail(table.encode('utf-8'))