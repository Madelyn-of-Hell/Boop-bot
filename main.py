from tokens import TOKEN
import discord
import random
import json
try: 
    with open('db.json','x') as f: pass
    with open('db.json','w') as f:
        f.write('{"":0}')
except: pass
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

    with open('db.json', 'r') as f:
        db = json.load(f)
    try: db[f'{victim}'] += 1
    except: db[f'{victim}'] = 1
    with open('db.json', 'w') as f:
        json.dump(db, f)
    await victim.send(f'You have been booped by {attacker}. You have been booped {db[f'{victim}']} times.',
                        file=random.choice(boops))


client.run(TOKEN)