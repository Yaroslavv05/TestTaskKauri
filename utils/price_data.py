from typing import Dict, Optional

price_data: Dict[str, Dict[str, float]] = {
    'binance': {},
    'kraken': {}
}

def update_price_data(exchange: str, pair: str, avg_price: float):
    if exchange not in price_data:
        price_data[exchange] = {}
    price_data[exchange][pair] = avg_price
    print(f"Updated {exchange} data: {pair} - {avg_price}")

def get_prices(pair: Optional[str] = None, exchange: Optional[str] = None) -> Dict[str, float]:
    result: Dict[str, float] = {}
    if exchange and pair:
        if exchange in price_data and pair in price_data[exchange]:
            result[pair] = price_data[exchange][pair]
    elif exchange:
        if exchange in price_data:
            result.update(price_data[exchange])
    elif pair:
        for ex in price_data:
            if pair in price_data[ex]:
                result[pair] = price_data[ex][pair]
    else:
        for ex in price_data:
            result.update(price_data[ex])
    return result
