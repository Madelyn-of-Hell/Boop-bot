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
        discord.File(fp='Boops/White1.gif'),
        discord.File(fp='Boops/White2.gif'),
        discord.File(fp='Boops/Black1.gif'),
        discord.File(fp='Boops/Black2.gif'),
        discord.File(fp='Boops/Orange1.gif'),
        discord.File(fp='Boops/Orange2.gif')
        ]
@client.event
async def on_message(message):
    if '!boop' in message.content and message.content[0] == '!':
        await message.delete()
        await attack(int(message.content[8:-1]),message.author, [1,0,0,0,'Booped'])
    if '!explode' in message.content and message.content[0] == '!':
        await message.delete()
        await attack(int(message.content[11:-1]),message.author, [0,1,0,1,'Exploded'])
    if '!implode' in message.content and message.content[0] == '!':
        await message.delete()
        await attack(int(message.content[11:-1]),message.author, [0,0,1,2,'Imploded'])

async def attack(victim: str, attacker, attackType:list[int, str]):
    victim = await client.fetch_user(victim)

    with open('db.json', 'r') as f:
        db = json.load(f)
    try: db[f'{victim}'][attackType[3]] += 1
    except: db[f'{victim}'] = [attackType,attackType,attackType]

    with open('db.json', 'w') as f:
        json.dump(db, f)
    await victim.send(f'You have been {attackType[4]} by {attacker}. You have been {attackType[4]} {db[f"{victim}"][attackType[3]]} times.',)


client.run(TOKEN)