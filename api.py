from fastapi import FastAPI
from host_checker import check_and_correct_host, is_alive_host

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/healthz")
async def root(hostname):
    if not hostname:
        return {"message": "Invalid Hostname"}
    hostname = check_and_correct_host(hostname)
    alive = is_alive_host(hostname)    
    return {"status": "up" if alive else "down"}
