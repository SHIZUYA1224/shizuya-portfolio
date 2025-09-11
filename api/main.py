from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="SHIZUYA Portfolio API",
    description="3D/Unity/AI作品用API",
    version="1.0.0"
)

# ==== ダミーデータ ====
class Item(BaseModel):
    id: int
    name: str
    price: int
    tags: List[str] = []

DB = {
    1: Item(id=1, name="3D Character #01", price=0, tags=["WIP", "Blender", "Unity"]),
    2: Item(id=2, name="Portfolio Site",   price=0, tags=["GitHub Pages", "HTML", "CSS"]),
    3: Item(id=3, name="FastAPI Demo",     price=0, tags=["API", "Python", "Uvicorn"]),
}

# ==== 既存 ====
@app.get("/")
def read_root():
    return {"message": "SHIZUYA Portfolio API", "status": "running"}

@app.get("/hello")
def read_hello():
    return {"message": "Hello, FastAPI!"}

# ==== 追加: 一覧取得 ====
@app.get("/items", response_model=List[Item])
def list_items(
    q: Optional[str] = Query(None, description="名前・タグを部分一致検索")
):
    items = list(DB.values())
    if q:
        q_low = q.lower()
        items = [
            it for it in items
            if (q_low in it.name.lower()) or any(q_low in t.lower() for t in it.tags)
        ]
    return items

# ==== 追加: 個別取得 ====
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = DB.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    return item