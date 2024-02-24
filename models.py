from sqlalchemy import Table, Column, Integer, String, Boolean, Float
from database import metadata

items = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('description', String(250)),
    Column('price', Float),
    Column('in_stock', Boolean)
)
