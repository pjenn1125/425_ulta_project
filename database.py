# Author: Chandler Harris
# Date: 10/20/2026
# File: database.py
# Description:

from pathlib import Path

from sqlalchemy import event
from sqlalchemy.engine import URL
from sqlmodel import SQLModel, Session, create_engine, select

from users.models import Role


DATABASE_PATH = Path(__file__).resolve().parent / "Database" / "ulta.sqlite"
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    URL.create("sqlite", database=str(DATABASE_PATH)),
    connect_args={"check_same_thread": False}
)


@event.listens_for(engine, "connect")
def enable_sqlite_foreign_keys(connection, _):
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    project_roles = (
        (1, "Admin", "Full system access"),
        (2, "Manager", "Manages products, inventory, and orders"),
        (3, "Employee", "Views products, inventory, and orders"),
    )
    with Session(engine) as session:
        for role_id, role_name, description in project_roles:
            role = session.exec(
                select(Role).where(Role.role_name == role_name)
            ).first()
            if role is None:
                conflicting_role = session.get(Role, role_id)
                if conflicting_role is not None:
                    raise RuntimeError(
                        f"Cannot seed role {role_name!r}: role ID {role_id} "
                        f"is already assigned to {conflicting_role.role_name!r}"
                    )
                session.add(
                    Role(
                        role_id=role_id,
                        role_name=role_name,
                        description=description,
                    )
                )
        session.commit()


def get_session():
    with Session(engine) as session:
        yield session
