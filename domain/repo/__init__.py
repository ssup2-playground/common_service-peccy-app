import yaml

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database

with open('config.yml', 'r', encoding="utf-8") as file:
    config = yaml.safe_load(file)
db_username = config["mysql_user"]
db_password = config["mysql_password"]
db_host = config["mysql_url"]
db_port = config["mysql_port"]
db_name = config["mysql_db_name"]

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
