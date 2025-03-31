# make sure all SQLModel models are imported before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# and alembic can't create migrations

from sqlmodel import SQLModel


from auth.schemas import *