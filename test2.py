from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputPeerChat

# Ganti dengan informasi sesi Anda
api_id = "17612509"
api_hash = "5d987f53b6ef5df97f05388828ba3f09"

chats = ['SoodLayer2024']

session_string = 'your_session_string'

# Ganti dengan ID grup yang ingin Anda pantau
group_id = '1656573810'

# Inisialisasi Telegram Client
client = TelegramClient('name', api_id, api_hash)

# Fungsi untuk menangani pesan yang diterima
async def handle_message(event):
    sender = await event.get_sender()
    print(f"{sender.first_name}: {event.message.message}")

# Mulai sesi Telegram Client
async def main():
    async with client:
        # Dapatkan objek InputPeer untuk grup chat
        entity = await client.get_input_entity(group_id)
        
        # Mulai mendengarkan pesan
        async for message in client.iter_messages(entity):
            await handle_message(message)

# Jalankan program utama
if __name__ == '_main_':
    client.loop.run_until_complete(main())