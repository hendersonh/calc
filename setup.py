from setuptools import setup, find_packages

setup(
    name="mycalc",
    version='0.1',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=[
        'Click' ,
        'pip>=19.0.3' ,
        'pytest' ,
        'pyinstaller'
    ],
    tests_require=['pytest', 'pytest-mock'],
    extras_require={'mongo': 'pymongo'},

    entry_points='''
        [console_scripts]
        mycalc=calc.cli:cli
    ''',
)
