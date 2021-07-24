import os
from . import BASE_DIR
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


def main():
    command_prefix = '>'
    client = commands.Bot(command_prefix=command_prefix)
    for fn in os.listdir(BASE_DIR / 'src' / 'cogs'):
        if fn.endswith('.py'):
            client.load_extension(f'src.cogs.{fn[:-3]}')
    client.run(os.environ.get('DISCORD_TOKEN'))


if __name__ == '__main__':
    main()
