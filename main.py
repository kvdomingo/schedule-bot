import click


@click.group()
def manage():
    pass


@click.command()
def runbot():
    from src import bot
    bot.main()


manage.add_command(runbot)


if __name__ == '__main__':
    manage()
