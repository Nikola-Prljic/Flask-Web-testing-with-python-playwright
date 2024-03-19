import sqlalchemy as mariadb

SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://niki:ktmsx@localhost/mydb'

# Test if it works
engine = mariadb.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
metadata = mariadb.MetaData()
division= mariadb.Table('users', metadata, autoload=True, autoload_with=engine)
print(repr(metadata.tables['divisions']))