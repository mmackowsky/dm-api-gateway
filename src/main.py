from fastapi import FastAPI, Request, Response, status

app = FastAPI()


@app.get("/api/users")
async def read_users():
    return {"users": []}
