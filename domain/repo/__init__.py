import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database

db_username = os.environ.get("MYSQL_USER", "root")
db_password = os.environ.get("MYSQL_PASSWORD", "root")
db_host = os.environ.get("MYSQL_URL", "127.0.0.1")
db_port = os.environ.get("MYSQL_PORT", "3306")
db_name = os.environ.get("MYSQL_DB_NAME", "peccy")

engine = create_engine(
    f"mysql+mysqldb://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}",
    pool_pre_ping=True,
)
if not database_exists(engine.url):
    create_database(engine.url)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
