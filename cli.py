import click
import calc

@click.group()
def cli():
    pass

@cli.command()
@click.argument('num1')
@click.argument('num2')
def add(num1, num2):
    calc.add(num1, num2)