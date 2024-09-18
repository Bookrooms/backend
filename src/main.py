from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from os import environ

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
    "http://localhost",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# db:5432 - service name from compose.yml
engine = create_engine(
    f"postgresql+psycopg://{environ['POSTGRES_USER']}:{environ['POSTGRES_PASSWORD']}@db:5432/{environ['POSTGRES_DB']}")

if not database_exists(engine.url):
    create_database(engine.url)

print("database_exists:", database_exists(engine.url))


@app.get("/api/test")
async def root():
    return { "message": "Hello World!" }


# declare after all others
app.mount("/", StaticFiles(directory="./dist", html = True), name="site")
