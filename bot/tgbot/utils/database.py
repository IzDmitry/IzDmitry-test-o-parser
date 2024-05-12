from sqlalchemy import create_engine, func, sql
from sqlalchemy.orm import sessionmaker
from .models import Product
from tgbot import config


class Database:
    def __init__(self,
                 db=config.MYSQL_DATABASE,
                 user=config.MYSQL_USER,
                 password=config.MYSQL_PASSWORD,
                 host=config.MYSQL_DB,
                 port=config.MYSQL_PORT):
        self._db = db
        self.engine = create_engine(
            f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}')
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
        closest_datetime = self.session.query(
            func.min(
                func.abs(
                    func.timestampdiff(
                        sql.text('SECOND'),
                        Product.date,
                        func.now()
                        )
                    )
                )
            ).scalar()
        closest_datetime_products = self.session.query(
            Product
            ).filter(func.abs(
                func.timestampdiff(
                    sql.text('SECOND'),
                    Product.date,
                    func.now()
                    )
                ) == closest_datetime).all()
        products_dict = {}
        for i, product in enumerate(closest_datetime_products, 1):
            products_dict[i] = {'name': product.name,
                                'url': product.url,
                                'date': product.date}
        return products_dict
