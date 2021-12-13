from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory='project/templates')
app.mount("/static", StaticFiles(directory="project//static"), name="static")


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(
        'home.html', context={'request': request})
