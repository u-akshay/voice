from gtts import gTTS
import os
from pyrogram import Client
from os import environ

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]

app = Client("my_bot",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token)

language = 'en'

@app.on_message()
def message(client, message):
    a = gTTS(text=message.text, lang=language, slow=False)
    a.save("welcome.ogg")
    app.send_audio(message.from_user.id, "welcome.ogg")
    print(message.text,'======', message.from_user.first_name)
app.run()

