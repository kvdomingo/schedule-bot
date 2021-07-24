import aiohttp
import requests

BASE_URL = 'https://squadtime-api.herokuapp.com/v1.0'


async def _arequest(endpoint: str, method: str = 'get', body: dict = None):
    async with aiohttp.ClientSession() as session:
        api = getattr(session, method)
        async with api(f'{BASE_URL}/{endpoint}', data=body) as res:
            if method in ['post', 'patch']:
                return await res.json(), res.status
            if method == 'delete':
                return [], res.status
            return await res.json()


class Api:
    @staticmethod
    async def events():
        return await _arequest('event')
