from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

app = FastAPI()


@app.get("/", include_in_schema=False)
async def redirect_to_helloworld():
    logger.info("Root (/) endpoint hit — suggesting /helloworld")
    return JSONResponse({"hint": "Try /helloworld"})


@app.get("/helloworld", response_class=JSONResponse)
async def read_root(request: Request):
    logger.info("/helloworld hit from %s", request.client.host)
    return {"status": "OK"}


@app.get("/health", response_class=JSONResponse)
async def health_check(request: Request):
    logger.info("/health hit from %s", request.client.host)
    return {"status": "healthy"}