from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# If you want to serve static assets (CSS, JS, images)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Option 1: Serve the HTML directly as a response
@app.get("/", response_class=HTMLResponse)
async def serve_flashcards():
    with open("flashcards.html", "r") as f:
        content = f.read()
    return content

# Option 2: If you want to use templates
# templates = Jinja2Templates(directory="templates")
# @app.get("/template", response_class=HTMLResponse)
# async def serve_from_template(request: Request):
#     return templates.TemplateResponse("flashcards.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)