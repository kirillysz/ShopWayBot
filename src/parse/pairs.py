from aiohttp import ClientSession

from config import config

async def parse_kzt_to_rub():
    url = f"https://v6.exchangerate-api.com/v6/{config.EXCHANGE_TOKEN}/latest/KZT"

    async with ClientSession() as session:
        async with session.get(url=url) as response:
            data = await response.json()

            return data["conversion_rates"].get("RUB")
        