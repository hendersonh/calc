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
@click.option('--n', '-n', type=(int, int))
def sub(n):
    """Enter <-n> follow by two number; we will subtract 2nd number from 1st number"""
    result = calc.sub(n[0], n[1])
    print('{} - {} = {}'.format(n[0], n[1], result))
     