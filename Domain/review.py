from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Text, Float

Base = declarative_base()

class Review(Base):
    __tablename__ = 'review'
    review_id = Column(Integer, primary_key=True)
    client_first_name = Column(String, nullable=False)
    review_content = Column(Text, nullable=False)
    stars = Column(Float, nullable=False)

    def __str__(self):
        return (f'review id: {self.review_id}\n'
                f'client_first_name: {self.client_first_name}\n'
                f'review_content: {self.review_content}\n'
                f'stars: {self.stars}')