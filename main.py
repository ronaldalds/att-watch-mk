import os
from fastapi import FastAPI, Header, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.controller.watch_controller import handle_start_watch
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title='API Att Token Watch no ERP MKSolutions', version="0.1.0")

@app.post("/watch/{item_id}")
async def read_item(item_id: int, Authorization: str = Header(None)):
    if Authorization == os.getenv('AUTH_TOKEN'):
        response = handle_start_watch(item_id)
        if response:
            return JSONResponse(content=jsonable_encoder({"status": response}), status_code=200)
        else:
            return JSONResponse(content=jsonable_encoder({"status": response}), status_code=404)
    else:
        return JSONResponse(content=jsonable_encoder({"status": "Error Authorization"}), status_code=401)
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8002)