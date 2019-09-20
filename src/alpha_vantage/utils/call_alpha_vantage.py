from common.utils.get_secrets import get_api_key

import requests

def api_get_req(stock_symbol: str):
    api_key = get_api_key("alpha_vantage")
    return requests.get(
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={api_key}",
        timeout=10,
    )
