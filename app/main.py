from fastapi import FastAPI
from app.redis_client import get_redis

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + Redis is running 🚀"}

@app.get("/count")
def count():
    r = get_redis()
    r.incr("visits")
    return {"visits": int(r.get("visits"))}