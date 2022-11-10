from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from connect_db import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    date_of_registration = Column(DateTime, default=datetime.now) # определение часового пояса???
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=True, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def chec_password(self, password):
        return check_password_hash(password)

    def __repr__(self):
        return f'<User {self.name} {self.email}>'


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    mood = Column(String(50), nullable=False)
    dairy_entry = Column(String, nullable=False)
    date_added = Column(DateTime, default=datetime.now) # определение часового пояса???
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'<Note {self.date_added} {self.dairy_entry}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
