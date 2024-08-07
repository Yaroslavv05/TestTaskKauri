from fastapi import APIRouter, HTTPException
from utils.price_data import get_prices

router = APIRouter()

@router.get("/prices")
async def get_prices_endpoint(pair: str = None, exchange: str = None):
    if pair:
        pair = pair.upper()
        if exchange:
            exchange = exchange.lower()
            if exchange == "binance":
                pair = pair.replace("/", "")
            elif exchange != "kraken":
                pair = pair.replace("/", "")
    
    prices = get_prices(pair=pair, exchange=exchange)
    
    if not prices:
        raise HTTPException(status_code=404, detail="Not found")
    
    return prices