from enum import Enum
from os.path import abspath, dirname, join

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import transforms

current_dir = dirname(abspath(__file__))
static_path = join(current_dir, "static")

app = FastAPI()
app.mount("/ui", StaticFiles(directory=static_path), name="ui")


@app.get("/")
def root():
    html_path = join(static_path, "index.html")
    return FileResponse(html_path)


class TransformerFunction(str, Enum):
    CLAPIFY = "clapify"
    BINARIZE = "binarize"
    EMOJIFY = "emojify"
    EXCLAMIFY = "exclamify"
    MYSTERY = "mystery"


@app.get("/transform")
def transform(function: TransformerFunction, text: str):
    """Transform the given text with one of the possible functions.
    Example query:
    /transform?function=clapify&text=Just%20do%20it
    """
    return {"transformed": getattr(transforms, function)(text)}
