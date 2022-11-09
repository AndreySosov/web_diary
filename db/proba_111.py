# db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


import config
# from connect_db import conn, cursor
from create_db import create_db


# conn = conn
# cursor = cursor
try:
    engine = create_engine(f'postgresql+psycopg2://{config.USER_DB}:{config.PASS_DB}'
                       f'@{config.HOST}:{config.PORT}/{config.DB_NAME}',
                       pool_pre_ping=True)
    engine.connect()

    db_session = scoped_session(sessionmaker(bind=engine))

    Base = declarative_base()
    Base.query = db_session.query_property()

except:
    create_db()




