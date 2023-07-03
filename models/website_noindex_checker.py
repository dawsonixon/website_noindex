from odoo import models
import requests
from bs4 import BeautifulSoup

class WebsiteNoindexChecker(models.Model):
    _name = 'website.noindex.checker'

    def check_noindex(self):
        # Lista stron, które chcesz sprawdzić
        urls = ['http://your-odoo-url.com/page1', 'http://your-odoo-url.com/page2']

        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tag = soup.find('meta', attrs={'name': 'robots'})

            if meta_tag and 'noindex' in meta_tag.get('content', ''):
                # Tutaj możemy na przykład utworzyć log
                self.env['website.noindex.log'].create({
                    'page_url': url,
                    'has_noindex': True,
                })
            else:
                self.env['website.noindex.log'].create({
                    'page_url': url,
                    'has_noindex': False,
                })

