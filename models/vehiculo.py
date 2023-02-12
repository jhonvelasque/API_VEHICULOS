from config.databases import Base 
from sqlalchemy import Column, Integer, String, Float,Date ,Table
from config.databases import meta

sede=Table("sede",meta)

"""
class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Date)
    rating = Column(Float)
    category = Column(String)
"""