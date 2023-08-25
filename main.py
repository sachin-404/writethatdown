import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

DB_CON_KEY = os.getenv('DB_KEY')
db_connection = MongoClient(DB_CON_KEY)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = db_connection.notes.notes.find({})
    for doc in docs:
        print(doc)
    return templates.TemplateResponse("index.html", {"request": request})
