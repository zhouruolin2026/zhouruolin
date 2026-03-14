# fastapi - 现代 Web 框架
# FastAPI 是基于 Python 的现代 Web 框架。
# 使用类型提示，支持异步。
# 自动生成 API 文档。
# 需要安装：pip install fastapi uvicorn

# 示例代码：创建简单 API
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 要运行服务器，使用：uvicorn main:app --reload
# 其中 main 是文件名 (如果文件名为 fastapi.py，则 uvicorn fastapi:app --reload)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)