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
tree = discord.app_commands.CommandTree(client)

db:dict = {}

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object())
    print("Ready!")
boops = [
        discord.File(fp='Boops/White1.gif'),
        discord.File(fp='Boops/White2.gif'),
        discord.File(fp='Boops/Black1.gif'),
        discord.File(fp='Boops/Black2.gif'),
        discord.File(fp='Boops/Orange1.gif'),
        discord.File(fp='Boops/Orange2.gif')
        ]

async def boop(type, victim, attacker):
    if type == 1:
        await attack(victim, attacker, 0)
    elif type == 2:
        await attack(victim, attacker, 1)
    elif type == 3:
        await attack(victim, attacker, 2)

async def attack(victim, attacker, attackType:int):
    attacks = ['booped','exploded','imploded']
    with open('db.json', 'r') as f:
        db = json.load(f)
    try: db[f'{victim}'][attackType] += 1
    except: 
        db[f'{victim}'] = [0,0,0]
        db[f'{victim}'][attackType] += 1



    with open('db.json', 'w') as f:
        json.dump(db, f)
    await victim.send(f'You have been {attacks[attackType]} by <@{attacker}>. You have been {attacks[attackType]} {db[f"{victim}"][attackType]} times.',)

@tree.command(
    name="boop",
    description="Boops a given target"
)
async def boop_target(interaction, target: discord.Member):
    await boop(1, target, interaction.user.id)
    await interaction.response.send_message(f'Succesfully Booped {target.name.capitalize()}')

@tree.command(
    name="explode",
    description="'Explodes' a given target"
)
async def first_command(interaction, target: discord.Member):
    await boop(2, target, interaction.user.id)
    await interaction.response.send_message(f'Succesfully Exploded {target.name.capitalize()}')
@tree.command(
    name="implode",
    description="'Implodes' a given target"
)
async def first_command(interaction, target: discord.Member):
    await boop(3, target, interaction.user.id)
    await interaction.response.send_message(f'Succesfully Booped {target.name.capitalize()}')

client.run(TOKEN)
