import asyncio
import threading
import uvicorn
from fastapi import FastAPI
from websocket.binance_websocket import binance_websocket
from websocket.kraken_websocket import kraken_websocket
from api.v1.endpoints import router as get_price

app = FastAPI()
app.include_router(router=get_price)

def start_websocket_clients():
    asyncio.run(run_websocket_clients())

async def run_websocket_clients():
    await asyncio.gather(
        binance_websocket(),
        kraken_websocket()
    )

if __name__ == "__main__":
    websocket_thread = threading.Thread(target=start_websocket_clients, daemon=True)
    websocket_thread.start()

    uvicorn.run(app, host="0.0.0.0", port=8000)
