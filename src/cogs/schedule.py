import discord
from discord.ext import commands
from datetime import datetime
from ..utils.endpoints import Api


class Schedule(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client

    @commands.group()
    async def schedule(self, ctx):
        pass

    @schedule.command(aliases=['show', 'list'])
    async def schedule_show(self, ctx):
        events = await Api.events()
        description = ''
        for event in events:
            date = event['date'][:-6]
            date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
            date = date.strftime('%d %b | %H:%M')
            description += f"`[{date}]` "
            description += f"**{event['group'].upper()}** "
            description += f"{event['name']}\n"
        embed = discord.Embed(
            title='Upcoming events',
            description=description,
        )
        embed.set_footer(text='All times shown in KST (UTC+9)')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Schedule(client))
