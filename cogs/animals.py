from nextcord.ext import commands
import nextcord
import sqlite3
from dotenv import load_dotenv
import os
import random


class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["doggo", "pupper"])
    async def dog(self, ctx):
        await ctx.send(embed=get_animal_picture(ctx, "dog"))

    @commands.command()
    async def cat(self, ctx):
        await ctx.send(embed=get_animal_picture(ctx, "cat"))

    @commands.command(aliases = ["quack", "ducky"])
    async def duck(self, ctx):
        await ctx.send(embed=get_animal_picture(ctx, "duck"))

def setup(bot):
    bot.add_cog(Animals(bot))
    load_dotenv()

def get_animal_picture(ctx, animal):
        conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
        c = conn.cursor()
        c.execute(f"SELECT url FROM animals WHERE type = '{animal}'")
        results = c.fetchall()
        random_choice=random.choice(results)
        embed = nextcord.Embed(title=f'{animal.title()} picture for {ctx.author.name}', color=0x03b2f8)
        embed.set_image(url=random_choice[0])
        conn.close()
        return embed