from telethon import TelegramClient, events
import os
import json

# Load from environment variables or config
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")  # without @
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")  # with @

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        if event.media:
            await client.send_file(TARGET_CHANNEL, file=event.media, caption=event.text)
        else:
            await client.send_message(TARGET_CHANNEL, event.text)
    except Exception as e:
        print(f"Error forwarding message: {e}")

print("Bot is running...")
client.start()
client.run_until_disconnected()
