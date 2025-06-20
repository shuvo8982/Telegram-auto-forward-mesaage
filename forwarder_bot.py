from telethon import TelegramClient, events
from telethon.sessions import StringSession  # ✅ এই লাইন যোগ করা হয়েছে

# ✅ তোমার দেওয়া ইনফো
API_ID = 27460522
API_HASH = "df6ee4a8ad244122fdb0a6990be3620a"
SESSION_STRING = "1BVtsOMMBu2YMTeWAd9ZLqdDROzGB3xdU1lMuucM-QUdphvqvufNjpPzLGK19wiQn80fBac4SBc0dQHTnS4uE2NxEiy4Zw6WGD02Jh8wX67mOV1VBi_Xs53NnlZ7U2cqLajigzewF1t15tjuEEStwzQv_jW7LWjJlLeAFHqnA4_AEIxgNvMRHH6GHOTC_FhpwCpO45Tc8pn2gO93ZZ4W6V2OHrw43Bg-UmRXMO7WZpvNgNmmdHchGAyNOH1Z_SzYgv42KoNRkHdq3LnRvi7b6ZKIlfXMKixbZWeSvcjOnU0AXg93w6HOJVa5KcSj4mD3azk44Dn7uMNZd3QdT90kEgB9gFr3xT2w="
SOURCE_CHANNEL = -1002524353308
TARGET_CHANNEL = -1001721353807

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_handler(event):
    try:
        if event.media:
            await client.send_file(TARGET_CHANNEL, event.media, caption=event.text or "")
        else:
            await client.send_message(TARGET_CHANNEL, event.text or "")
        print("✅ ফরওয়ার্ড হয়েছে")
    except Exception as e:
        print("⚠️ ফরওয়ার্ড করতে সমস্যা:", e)

print("🤖 Bot is running... Ctrl+C দিলে বন্ধ হবে")
client.start()
client.run_until_disconnected()
