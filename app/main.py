from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevOps Agent Demo Running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
