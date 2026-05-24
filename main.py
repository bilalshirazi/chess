from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from openings_data import OPENINGS

app = FastAPI(title="Chess Academy")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

BASE = ""  # empty for local dev; static build uses /chess


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    openings = list(OPENINGS.values())
    return templates.TemplateResponse(
        "index.html", {"request": request, "openings": openings, "base": BASE}
    )


@app.get("/opening/{opening_id}", response_class=HTMLResponse)
async def opening(request: Request, opening_id: str):
    opening = OPENINGS.get(opening_id)
    if not opening:
        return HTMLResponse("<h1>Opening not found</h1>", status_code=404)
    return templates.TemplateResponse(
        "opening.html", {"request": request, "opening": opening, "base": BASE}
    )


@app.get("/pgn", response_class=HTMLResponse)
async def pgn_viewer(request: Request):
    return templates.TemplateResponse(
        "pgn.html", {"request": request, "base": BASE}
    )


@app.get("/api/opening/{opening_id}")
async def opening_api(opening_id: str):
    opening = OPENINGS.get(opening_id)
    if not opening:
        return JSONResponse({"error": "not found"}, status_code=404)
    return opening
