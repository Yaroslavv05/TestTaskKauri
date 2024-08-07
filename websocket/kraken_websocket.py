import websockets
from services.kraken_service import process_kraken_message, format_kraken_pairs
from core.config import settings
import aiohttp
import json
import asyncio

async def fetch_kraken_pairs():
    url = 'https://api.kraken.com/0/public/AssetPairs'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            pairs = list(data['result'].keys())
            return await format_kraken_pairs(pairs)

async def kraken_websocket():
    url = settings.KRAKEN_WEBSOCKET_URL
    pairs = await fetch_kraken_pairs()
    async with websockets.connect(url) as websocket:
        print("Connected to Kraken WebSocket")
        subscribe_message = {
            "event": "subscribe",
            "pair": pairs[:697],
            "subscription": {"name": "ticker"}
        }
        await websocket.send(json.dumps(subscribe_message))
        while True:
            message = await websocket.recv()
            await process_kraken_message(message)


if __name__ == "__main__":
    asyncio.run(kraken_websocket())
