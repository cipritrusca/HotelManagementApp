from sqlalchemy.ext.declarative import declarative_base
from Domain.clients import Client
from Domain.room import Room
from sqlalchemy import Column, Integer, ForeignKey, Date

Base = declarative_base()

class Reservation(Base):
    __tablename__ = 'reservation'
    reservation_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey(Client.client_id), nullable=False)
    room_number = Column(Integer, ForeignKey(Room.room_number), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    def __str__(self):
        return (f"reservation_id: {self.reservation_id}\n"
                f"client_id: {self.client_id}\n"
                f"room_number: {self.room_number}\n"
                f"start_date: {self.start_date}\n"
                f"end_date: {self.end_date}")

    def return_reservations_as_dict(self):
        return {
            'reservation id': self.reservation_id,
            'client id': self.client_id,
            'room number': self.room_number,
            'start date': self.start_date,
            'end date': self.end_date
        }