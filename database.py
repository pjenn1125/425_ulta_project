# Author: Chandler Harris
# Date: 10/20/2026
# File: database.py
# Description:

from sqlmodel import SQLModel, Session, create_engine

sqlite_file_name = "ulta.sql"
sqlite_url = "sqlite:///" + sqlite_file_name

engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

