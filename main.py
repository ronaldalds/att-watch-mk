from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.controller.watch_controller import handle_start_watch

app = FastAPI()

@app.get("/watch/{item_id}")
async def read_item(item_id: int):
    response = handle_start_watch(item_id)
    if response:
        return JSONResponse(content=jsonable_encoder({"status": response}), status_code=200)
    else:
        return JSONResponse(content=jsonable_encoder({"status": response}), status_code=404)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8010)