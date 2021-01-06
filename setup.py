from setuptools import setup

setup(
    name='LinLin',
    version='0.1',
    py_modules=['_func2commands'],
    install_requires=[
        'Click',
    ],

    ## 主要是这里
    entry_points='''
        [console_scripts]
        LinLin=_func2commands:cli
    ''',
)