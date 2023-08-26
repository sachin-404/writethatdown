import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pymongo import MongoClient

load_dotenv()

app = FastAPI()

DB_CON_KEY = os.getenv('DB_KEY')
db_connection = MongoClient(DB_CON_KEY)
