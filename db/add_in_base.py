from connect_db import db_session
from models import User, Note


def add_user(name: str, email: str, password: str):
    first_user = User(name=name, email=email, password=password)
    db_session.add(first_user)
    db_session.commit()


def add_note(mood: str, note: str):
    note = Note(mood=mood, dairy_entry=note)
    db_session.add(note)
    db_session.commit()


add_user('vasia', 'sdaf@sdg.rt', '123qwe')