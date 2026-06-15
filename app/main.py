from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, restaurants, menu, orders

app = FastAPI(title="Kryme Lavka — Доставка еды", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Авторизация"])
app.include_router(restaurants.router, prefix="/restaurants", tags=["Рестораны"])
app.include_router(menu.router, prefix="/menu", tags=["Меню"])
app.include_router(orders.router, prefix="/orders", tags=["Заказы"])

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в Kryme Lavka! 🍔🚀"}