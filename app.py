from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from datetime import datetime
from contextlib import contextmanager

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@contextmanager
def get_db():
    conn = sqlite3.connect('prompts.db')
    conn.row_factory = sqlite3.Row  # 辞書形式で取得
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                model TEXT,
                time TEXT NOT NULL
            )
        """)
        conn.commit()

init_db()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request, q: str = None):
    with get_db() as conn:
        if q:
            prompts = conn.execute(
                "SELECT * FROM prompts WHERE content LIKE ? ORDER BY time DESC",
                (f'%{q}%',)
            ).fetchall()
        else:
            prompts = conn.execute("SELECT * FROM prompts ORDER BY time DESC").fetchall()
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prompts": prompts,
        "query": q or ""
    })

@app.post("/save")
async def save(content: str = Form(...), model: str = Form("unknown")):
    if not content.strip():
        raise HTTPException(400, "Content cannot be empty")
    
    with get_db() as conn:
        conn.execute(
            "INSERT INTO prompts (content, model, time) VALUES (?, ?, ?)",
            (content, model, datetime.now().strftime("%Y-%m-%d %H:%M"))
        )
        conn.commit()
    
    return {"status": "saved"}

@app.delete("/delete/{id}")
async def delete(id: int):
    with get_db() as conn:
        conn.execute("DELETE FROM prompts WHERE id = ?", (id,))
        conn.commit()
    
    return {"status": "deleted"}

@app.get("/export")
async def export():
    import json
    with get_db() as conn:
        prompts = conn.execute("SELECT * FROM prompts").fetchall()
    
    return [dict(p) for p in prompts]
  
