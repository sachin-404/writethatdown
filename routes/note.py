from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import db_connection
from schema.note import noteEntity, notesEntity

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = db_connection.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "description": doc["description"],
            "important": doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def create_note(request: Request):
    form = await request.form()
    form_dict = dict(form)
    form_dict["important"] = True if form_dict.get("important") == "on" else False
    note = db_connection.notes.notes.insert_one(form_dict)
    return {"Success": True}