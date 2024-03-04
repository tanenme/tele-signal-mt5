from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = '17612509'
api_hash = '5d987f53b6ef5df97f05388828ba3f09'
session_file = './test.session'
group_name = 'nama_grup'

async def main():
    async with TelegramClient(StringSession(session_file), api_id, api_hash) as client:
        async for dialog in client.iter_dialogs():
            print(dialog)

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
