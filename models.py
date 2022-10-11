
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAM, Boolean, ForeinKey, DECIMAL

Base = declarative_base()


class User(Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    email = Column(VARCHAR(20), nullable=False, unique=True)
    date_created = Column(TIMESTAM, default=datetime.now())



class Category(Base):
    __tablename__: str = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    is_published = Column(Boolean, default=False)


class Product(Base):
    __tablename__: str = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(20), nullable=False)
    descr = Column(VARCHAR(140), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    is_published = Column(Boolean, default=False)
    category_id = Column(Integer,
        ForeinKey('categories.id', ondelete='CASCADE'),
        nullbale=False
    )