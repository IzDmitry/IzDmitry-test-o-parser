from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .models import Product
from tgbot import config


class Database:

    def __init__(self, db='django_backend',
                       user='django', 
                       password='mysql1234pass', 
                       host='db', 
                       port=3306):
        self._db = db
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def close(self):
        if self.session:
            self.session.commit()
            self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def session(func):
        def wrapper(self, *args, **kwargs):
            try:
                result = func(self, *args, **kwargs)
                self.session.commit()
                return result
            except:
                self.session.rollback()
                raise
            finally:
                self.session.close()
        return wrapper


    @session
    def get_products(self):
        closest_date = self.session.query(func.min(func.abs(func.datediff(Product.date, datetime.now())))).scalar()
        closest_date_products = self.session.query(Product).filter(func.abs(func.datediff(Product.date, datetime.now())) == closest_date).all()
        
        products_dict = {}
        for i, product in enumerate(closest_date_products, 1):
            products_dict[i] = {'name': product.name, 'url': product.url, 'date': product.date}
        
        return products_dict
