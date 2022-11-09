import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import config


try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(user=config.USER_DB,
                           # пароль, который указали при установке PostgreSQL
                           password=config.PASS_DB,
                           host=config.HOST,
                           port=config.PORT)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()
    sql_create_database = f'create database {config.DB_NAME}'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
# finally:
#     if conn:
#         cursor.close()
#         conn.close()
#         print("Соединение с PostgreSQL закрыто")

