import discord
from discord.ext import commands
from datetime import datetime


class Admin(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.time_up = datetime.now()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user}')
        await self.client.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Game(name='under development')
        )

    @commands.group(hidden=True)
    async def admin(self, ctx):
        pass

    @admin.command(aliases=['status'])
    async def admin_status(self, ctx):
        uptime = str(datetime.now() - self.time_up)
        embed = discord.Embed(
            title='Latest build',
            color=discord.Color.green(),
        )
        embed.add_field(
            name='Uptime',
            value=uptime,
            inline=False,
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))
