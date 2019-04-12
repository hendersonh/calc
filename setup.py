from setuptools import setup

setup(
    name="mycalc",
    version='0.1',
    py_modules=['calc'],
    install_requires=[
        'Click' ,
        'pip>=19.0.3' ,
        'pytest' ,
    ],
    entry_points='''
        [console_scripts]
        mycalc=calc:cli
    ''',
)