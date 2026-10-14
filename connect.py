import os
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION_STRING"]

client = TelegramClient(StringSession(session), api_id, api_hash)

async def main():
    await client.connect()
    if await client.is_user_authorized():
        me = await client.get_me()
        print("Connected:", me.username or me.id)
    else:
        print("Session is not authorized.")
    await client.disconnect()

import asyncio
asyncio.run(main())