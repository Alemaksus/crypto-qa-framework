from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Crypto QA Agent is up and running"}