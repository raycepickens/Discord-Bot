##import bot

from typing import Final
import os
from discord import Intents, Client, Message
from responses import handle_response

TOKEN = "ask creator for token"

intents: Intents = Intents.default()
intents.message_content= True  # NOQA
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str):
    if not user_message:
        print('message was empty')
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



@client.event
async def on_ready():
    print(f'{client.user} is now running')



@client.event

async def on_message(message: Message):
    if message.author == client.user:
        return
    
    user_message: str = message.content

    await send_message(message, user_message)



def main():
    client.run(token=TOKEN)


if __name__== "__main__":

    main()