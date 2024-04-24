# pip install fastapi uvicorn
# uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello"}

@app.get("/page1")
def greet():
    return {"message": "page1"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
