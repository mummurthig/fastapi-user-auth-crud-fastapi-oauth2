from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    try:
        return True
    
    except Exception as e:
        return str(e)