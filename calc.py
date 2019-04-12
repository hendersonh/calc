import click

@click.group()
def cli():
    pass

@cli.command()
#@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
#@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.argument('num1')
@click.argument('num2')
def add(num1, num2):
    """Will add two given numbers."""
    print('{} + {} = {}'.format(num1, num2, int(num1) + int(num2) ))  
