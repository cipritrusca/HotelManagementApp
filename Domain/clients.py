from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    client_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __str__(self):
        return(f'client id: {self.client_id}\n'
               f'first name: {self.first_name}\n'
               f'last_name: {self.last_name}\n'
               f'email: {self.email}')

    def __repr__(self):
        return(f'client id: {self.client_id}\n'
               f'first name: {self.first_name}\n'
               f'last_name: {self.last_name}\n'
               f'email: {self.email}')

    def return_client_as_dict(self):
        return {
            'client id': self.client_id,
            'first name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }