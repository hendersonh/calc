import pytest
import calc
import click

def test_calc_add():
    assert calc.add(5, 10) == 15


