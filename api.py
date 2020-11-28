from fastapi import FastAPI, Query
from host_checker import check_and_correct_host, is_alive_host
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, provide hostname=... to /healthz path"}


@app.get("/healthz")
def root(hostname=Query(None)):
    try:
        if not hostname:
            raise()
        hostname = check_and_correct_host(hostname)
        is_alive = is_alive_host(hostname)
        return {"status": "up" if is_alive else "down"}
    except Exception:
        return {"message": "Error, invalid hostname value"}
    

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="info")