from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

client = commands.Bot(command_prefix=os.getenv("DISCORD_PREFIX"))

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"loaded: {filename}")


client.run(os.getenv("DISCORD_TOKEN"))