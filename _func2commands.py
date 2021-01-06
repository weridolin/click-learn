import click

@click.group()
def cli():
    pass

@click.command()
def command_one():
    click.echo(f'this is command_one')

@click.command()
def command_two():
    click.echo(f'this is command_two')

@click.command()
@click.option('--var1',default=1,help="value1 of command_three")
@click.argument('var2')
def command_three(var1,var2):
    click.echo(f'>> this is command_three:{var1}:{var2}')


cli.add_command(command_one)
cli.add_command(command_two)
cli.add_command(command_three)
if __name__ == '__main__':
    cli()
