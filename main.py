from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from databases import Database
from sqlalchemy import Table, Column, Integer, String, Boolean, Float, MetaData, create_engine
from sqlalchemy.sql import select

# Define a Pydantic model that represents an item
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: bool

# Database setup
DATABASE_URL = "postgresql://admin_carvach:Helloworld%402001@moulik-task.postgres.database.azure.com:5432/postgres?sslmode=require"


database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
items = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('description', String(250)),
    Column('price', Float),
    Column('in_stock', Boolean)
)

# Create the table
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# CRUD operations
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    query = items.insert().values(id=item.id, name=item.name, description=item.description, price=item.price, in_stock=item.in_stock)
    await database.execute(query)
    return item

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = select([items]).where(items.c.id == item_id)
    result = await database.fetch_one(query)
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return result

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    query = items.update().where(items.c.id == item_id).values(name=item.name, description=item.description, price=item.price, in_stock=item.in_stock)
    await database.execute(query)
    return {**item.dict(), "id": item_id}

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {"message": "Item deleted successfully"}


