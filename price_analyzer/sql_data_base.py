from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('sqlite:///price_analyzer/search_history.db')
Base = declarative_base()

class PriceAnalyzer(Base):
    __tablename__ = "PriceList"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sql_input = Column("input", String)
    sql_name = Column("name", String)
    sql_price = Column("price", Float)
    sql_url = Column("url", String)
    sql_time = Column("create_at", DateTime, default=datetime.utcnow)

    def __init__(self, sql_input, sql_name, sql_price, sql_url):
        self.sql_input = sql_input
        self.sql_name = sql_name
        self.sql_price = sql_price
        self.sql_url = sql_url

    def __repr__(self):
        return f"{self.id} {self.sql_input} {self.sql_name} {self.sql_price} {self.sql_url} {self.sql_time}"

Base.metadata.create_all(engine)
