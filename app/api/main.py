import logging
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
import psycopg2 as pg

LOG = logging.getLogger()

# config
docs_url = "/docs"
redoc_url = "/redoc"
favicon_url = "/favicon.png"
description = "An example FastAPI templat"

# Initialize application
app = FastAPI(
    title="API",
    description=description,
    version="0.1.0",
    contact={
        "name": "",
        "email": "",
    },
    docs_url=None,  # Make these None so we can customize later
    redoc_url=None,
)

# app.include_router()

# Enable cors
# TODO make this less open for security reasons
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root
@app.get("/")
def default(req: Request):
    root_path = req.scope.get("root_path")
    return f"Welcome to the API! See {root_path+docs_url} for Swagger UI. See {root_path+redoc_url} for Redoc"


@app.get("/test-db")
def test_db(req: Request):
    try:
        conn = pg.connect(
            host=os.environ.get("POSTGRES_HOST"),
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
        )
        cur = conn.cursor()
        cur.execute("SELECT msg FROM example")
        res = cur.fetchall()[0][0]
        return str(res)
    except Exception as e:
        return f"Could not connect to DB host: {os.environ.get('POSTGRES_HOST')}, db: {os.environ.get('POSTGRES_DB')}, user: {os.environ.get('POSTGRES_USER')} - {e}"


# Make it pretty
@app.get(docs_url, include_in_schema=False)
def show_custom_swagger_ui(req: Request):
    return get_swagger_ui_html(openapi_url="openapi.json", title="API")


@app.get(redoc_url, include_in_schema=False)
def show_custom_redoc_ui(req: Request):
    return get_redoc_html(openapi_url="openapi.json", title="API")


# Custom Favicon
# @app.get(favicon_url)
# async def favicon():
#     return FileResponse("pathTo/favicon.png")
