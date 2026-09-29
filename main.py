import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Get absolute path to the directory where this main.py file is located
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Mount static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Configure Jinja2 HTML templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_landing_page(request: Request):
    return templates.TemplateResponse(
    request=request, 
    name="index.html"
)

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}
