import discord
import random
from discord import app_commands
from discord.ext import commands


# noinspection PyUnresolvedReferences
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} KILL IT!')

    @app_commands.command(name='ping', description='checks the bots ping')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'slow ass bot is running at **{round(self.bot.latency * 1000)}ms**')

    @app_commands.command(name='user', description='Displays information about a user')
    async def user(self, interaction: discord.Interaction, member: discord.Member = None):
        if member is None:
            member = interaction.user

        random_color = discord.Color(random.randint(0, 0xFFFFFF))
        embed = discord.Embed(
            title=f"User Info: {member.name}",
            color=random_color
        )
        embed.set_thumbnail(url=member.display_avatar.url)  # User avatar
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="User ID", value=member.id, inline=True)
        embed.add_field(name="Joined Server On", value=member.joined_at.strftime('%B %d, %Y'), inline=True)
        embed.add_field(name="Account Created On", value=member.created_at.strftime('%B %d, %Y'), inline=True)
        embed.add_field(name="Roles", value=', '.join(role.name for role in member.roles if role.name != "@everyone"),
                        inline=False)

        # Send the embed as the response
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="avatar", description="steals a users avatar")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):
        if member is None:
            member = interaction.user

        random_color = discord.Color(random.randint(0, 0xFFFFFF))
        embed = discord.Embed(color=random_color)
        embed.set_image(url=member.display_avatar)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))