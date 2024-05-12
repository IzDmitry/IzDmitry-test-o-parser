from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from difflib import SequenceMatcher
from selenium.webdriver.chrome.options import Options
from .models import Product


class Parser:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")

    def get_page(self, page):
        try:
            self.browser = webdriver.Remote(
               command_executor="http://selenium-hub:4444/wd/hub",
               desired_capabilities={
                        "browserName": "chrome",
                    })
            self.browser.get(page)
            self.browser.refresh()
            try:
                wait = WebDriverWait(self.browser, 5)
                wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#ozonTagManagerApp')
                ))
            except TimeoutException:
                print('The page could not load')
            html = self.browser.page_source
            self.browser.quit()
            return BeautifulSoup(html, features='html.parser')
        except Exception as e:
            print(e)

    def get_one_products(self, page):
        page = self.get_page(page)
        return page

    def get_products(self, page):
        page = self.get_page(page)
        search_result = page.find(
            'div',
            {'class': 'widget-search-result-container'}
        )
        items = next(search_result.children)

        return [item for item in items.contents if item.name == 'div']

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def find_similar_alt_image(self, item2, name):
        for img in item2.find_all('img'):
            alt_text = img.get('alt', '')
            if self.similar(alt_text, name) >= 0.5:
                return img
        return None

    def get_products_dict(self, page, count):
        date = datetime.now()
        items = self.get_products(page)
        saved_products = {}
        product_count = 0
        for item in items:
            name = item.find('span', {'class': 'tsBody500Medium'}).text
            price = item.find('span', {'class': 'tsHeadline500Medium'}).text
            discount_values = item.find_all('span',
                                            class_='tsBodyControl400Small')
            for i in range(1, len(discount_values), 2):
                discount = discount_values[i].text
            price = int(price.replace('\u2009', '').replace('₽', ''))
            link = 'https://ozon.ru' + item.find('a')['href']
            items2 = self.get_one_products(link)
            for item2 in items2:
                try:
                    description = item2.find(
                        'div',
                        {'id': 'section-description'}
                    ).find('div').find_next('div').text
                    first_image = self.find_similar_alt_image(item2, name)
                    if first_image:
                        first_image_url = first_image['src']
                except Exception as e:
                    print(e)
                    description = None
                    first_image_url = None
            product = Product(name=name, price=price,
                              description=description,
                              image_url=first_image_url, discount=discount,
                              url=link, date=date)
            product.save()
            saved_products[name] = {
                'price': price,
                'description': description,
                'image_url': first_image_url,
                'discount': discount
            }
            product_count += 1
            if product_count >= count:
                return saved_products

        return saved_products


if __name__ == '__main__':
    page = 'https://www.ozon.ru/seller/1/products/'
    parser = Parser()
    parser.get_products_dict(page)
