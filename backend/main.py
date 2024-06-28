from fastapi import FastAPI

from schema import CreateOrderRequest
from utils import create_order as create_order_in_db


app = FastAPI()


@app.get("/")
async def root():
    return "Server is up"


@app.post("/orders")
async def create_order(request: CreateOrderRequest):
    result = await create_order_in_db(request)
    return result


"""
curl --location 'localhost:8080/orders' \
--header 'Content-Type: application/json' \
--data '{
    "p_id": 3,
    "price": 100
}'
"""
