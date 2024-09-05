import discord
import random
from discord import app_commands
from discord.ext import commands

# noinspection PyUnresolvedReferences
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} KILL IT!')

    @app_commands.command(name='hello', description=':3')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'hiiiiiiii {interaction.user.mention} :3 ')

    @app_commands.command(name='fortune', description='tells your honest fortune')
    async def fortune(self, interaction: discord.Interaction):
        response = ['you will die alone', 'you have no friends', 'you will have a bald spot by 25',
                    'you will never please a woman', 'you have a small cock']
        await interaction.response.send_message(f"{random.choice(response)}")

    @app_commands.command(name='gay', description='gay check')
    async def gay(self, interaction: discord.Interaction, member: discord.Member = None):
        if member is None:
            member = interaction.user

        if member.id == 749378812776677406:
            response = f"{member.mention} is 100% gay :3 (teehee)"
        else:
            response = f"{member.mention} is {random.randint(0, 100)}% gay"

        await interaction.response.send_message(response)

async def setup(bot):
    await bot.add_cog(Fun(bot))