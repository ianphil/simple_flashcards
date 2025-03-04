from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import json

app = FastAPI()

# If you want to serve static assets (CSS, JS, images)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the HTML directly as a response
@app.get("/", response_class=HTMLResponse)
async def serve_flashcards():
    with open("flashcards.html", "r") as f:
        content = f.read()
    return content

# New endpoint to serve flashcard data
@app.get("/flashcards", response_class=JSONResponse)
async def get_flashcards():
    with open("flashcards.json", "r") as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
