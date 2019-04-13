import click
import calc

@click.group()
def cli():
    pass

@cli.command()
@click.argument('num1')
@click.argument('num2')
def add(num1, num2):
    result = calc.add(num1, num2)
    print('{} + {} = {}'.format(num1, num2, result))

@cli.command()
@click.argument('num1')
@click.argument('num2')
def sub(num1, num2):
    result = calc.sub(num1, num2)
    print('{} - {} = {}'.format(num1, num2, result))
     
