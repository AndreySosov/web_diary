from models import User, Note


def get_user():
    user = User.query.first()
    print(f"""Имя {user.name}
          Email {user.email}
          """)


def get_note():
    note = Note.query.first()
    print(f"""Дата записи {note.date_added}
              заметка дневника {note.dairy_entry}
              """)
