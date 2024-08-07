import asyncio
import websockets
from services.binance_service import process_binance_message
from core.config import settings

async def binance_websocket():
    async with websockets.connect(settings.BINANCE_WEBSOCKET_URL) as websocket:
        print("Connected to Binance WebSocket")
        while True:
            message = await websocket.recv()
            await process_binance_message(message)


if __name__ == "__main__":
    asyncio.run(binance_websocket())
