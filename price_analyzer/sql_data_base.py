from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('sqlite:///price_analyzer/search_history.db')
Base = declarative_base()

class PriceAnalyzer(Base):
    __tablename__ = "PriceList"
    id = Column(Integer, primary_key=True, autoincrement=True)
    input = Column("input", String)
    name = Column("name", String)
    price = Column("price", Float)
    time = Column("create_at", DateTime, default=datetime.utcnow)

    def __init__(self, input, name, price):
        self.input = input
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.input} - {self.name} {self.price}: {self.create_at}"

Base.metadata.create_all(engine)
