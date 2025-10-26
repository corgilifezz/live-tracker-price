import random
import time

from rich.console import Console
from rich.live import Live
from rich.table import Table
import ccxt

def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("Symbol")
    table.add_column("High")
    table.add_column("Low")
    table.add_column("Last")

    for symbol in ["BTC/USDT", "ETH/USDT", "DOGE/USDT"]:
        ticker = ccxt.bitfinex().fetch_ticker(symbol)
        table.add_row(
            f"{symbol}", f"{ticker['high']}", f"{ticker['low']}", f"{ticker['last']}"
        )
    return table

# console.clear()

with Live(generate_table(), refresh_per_second=1) as live:
    for _ in range(40):
        time.sleep(5)
        live.update(generate_table())

