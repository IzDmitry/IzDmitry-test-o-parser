from celery import shared_task
from .parser import Parser


@shared_task
def parce_product_task(products_count):
    """
    Функция для отпраки email.
    """
    parser = Parser()
    page = 'https://www.ozon.ru/seller/1/products/'
    print(page, products_count)
    product = parser.get_products_dict(page, products_count)
    return product
