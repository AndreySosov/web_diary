from models import User, Note

my_user = User.query.first()
print(f"""Имя: {my_user.name}
Email: {my_user.email}""")
