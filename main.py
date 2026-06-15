from fastapi import FastAPI

app = FastAPI(title="My First FastAPI App")

@app.get("/")
async def root():
    return {"message": "Привет! Моё приложение работает в интернете 🚀"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}