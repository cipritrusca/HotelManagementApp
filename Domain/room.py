from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'
    room_number = Column(Integer, primary_key=True, autoincrement=True)
    room_type = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    size = Column(Integer, nullable=False)
    has_view = Column(Boolean, nullable=False)

    def __str__(self):
        return (f'The room number: {self.room_number}\n'
                f'The room type: {self.room_type}\n'
                f'The price: {self.price_per_night}\n'
                f'Is it having a view? {self.has_view}')

    def return_rooms_as_dict(self):
        return {
            'room number': self.room_number,
            'room type': self.room_type,
            'price per night': self.price_per_night,
            'size': self.size,
            'has view': self.has_view
        }