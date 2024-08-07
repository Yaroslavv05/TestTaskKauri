from typing import List
import json
from utils.price_data import update_price_data

async def process_binance_message(message: str):
    data = json.loads(message)
    for item in data:
        pair = item['s']
        bid_price = float(item['b'])
        ask_price = float(item['a'])
        avg_price = (bid_price + ask_price) / 2
        update_price_data('binance', pair, avg_price)
