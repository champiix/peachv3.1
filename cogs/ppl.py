import discord
import random
from discord import app_commands
from discord.ext import commands


# noinspection PyUnresolvedReferences
class Ppl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} KILL IT!')

    @app_commands.command(name='zen', description=':^)')
    async def zen(self, interaction: discord.Interaction):
        zimage = ["https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907441/peach%20bot/jzjlhz4_m3xbcz.png",
                  "https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907492/peach%20bot/RUOWQcY_dyzyp7.png",
                  "https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907559/peach%20bot/Jefvl1j_kzbm1p.png",
                  "https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907617/peach%20bot/p1OeCRY_gwdthf.png",
                  "https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907659/peach%20bot/afZsnyH_jolvxn.png"]

        embed = discord.Embed()
        embed.set_image(url=random.choice(zimage))
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Ppl(bot))