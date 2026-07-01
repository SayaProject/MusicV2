import asyncio
from pyrogram import Client

API_ID = 30422005
API_HASH = "5170ded206641d73215baf40175a6924"

async def generate():
    async with Client("session_gen", api_id=API_ID, api_hash=API_HASH) as app:
        session = await app.export_session_string()
        print("\nYour Pyrogram Session String:\n")
        print(session)
        print("\nCopy this string and paste it into the SESSION variable in your .env file.\n")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate())
