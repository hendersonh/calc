import click

@click.group()
def cli():
    pass

@cli.command()
#@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
#@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.argument('num1', help="The first number")
@click.argument('num2', help="The sencond number")
def add(num1, num2):
    """Will add two given numbers."""
    print('{} + {} = {}'.format(num1, num2, num1 + num2 ))  
