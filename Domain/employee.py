from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    ocupation = Column(String, nullable=False)

    def __str__(self):
        return (f'employee id: {self.employee_id}\n'
                f'first_name: {self.first_name}\n'
                f'last_name: {self.last_name}\n'
                f'ocupation: {self.ocupation}')