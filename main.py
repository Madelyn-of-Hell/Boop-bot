from tokens import TOKEN
import discord
import random
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
db:dict = {}
discord.User
boops = [
        discord.File('Boops/White1.gif'),
        discord.File('Boops/White2.gif'),
        discord.File('Boops/Black1.gif'),
        discord.File('Boops/Black2.gif'),
        discord.File('Boops/Orange1.gif'),
        discord.File('Boops/Orange2.gif')
        ]
@client.event
async def on_message(message):
    if '!boop' in message.content and message.content[0]:
        await boop(int(message.content[8:-1]),message.author)

async def boop(victim: str, attacker):
    victim = await client.fetch_user(victim)
    await victim.send(f'You have been booped by {attacker}', file=random.choice(boops))

client.run(TOKEN)