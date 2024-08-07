import re
from typing import List
import json
from utils.price_data import update_price_data

async def format_kraken_pairs(pairs: List[str]) -> List[str]:
    formatted_pairs = []
    for pair in pairs:
        match = re.match(r'(.+)(USD|EUR|GBP|JPY|CAD|AUD|CHF|XBT|ETH|USDT|ZUSD)', pair)
        if match:
            formatted_pairs.append(match.group(1) + '/' + match.group(2))
        else:
            formatted_pairs.append(pair)
    return formatted_pairs

async def process_kraken_message(message: str):
    data = json.loads(message)
    if isinstance(data, list) and len(data) > 1 and isinstance(data[1], dict):
        item = data[1]
        pair = data[3] if isinstance(data[3], str) else "UNKNOWN"
        if 'b' in item and 'a' in item:
            bid = float(item['b'][0])
            ask = float(item['a'][0])
            avg_price = (bid + ask) / 2
            update_price_data('kraken', pair, avg_price)
