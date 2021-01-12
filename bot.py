import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_ID')
GENERAL = os.getenv('DISCORD_GENERAL_ID')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.id == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild: \n' 
        f'{guild.name} (id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
	channel = client.get_channel(int(GENERAL))
	await channel.send(f'Hello {member.name}! Please type the command: /nick FirstName LastName when you first join the server. And say what Group you are in (Group A or Group B). Also, tell me about yourself. What makes you, you? What is your favorite board game? Do you play video games? If so, what do you enjoy playing? I would really like us to be a close-knit team!')
client.run(TOKEN)
