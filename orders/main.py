from fastapi import FastAPI
from api.orders import router as order_router

app = FastAPI()
app.include_router(order_router)