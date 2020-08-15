from setuptools import setup

setup(
    name="clemail",
    version="0.1",
    py_modules=['clemail'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clemail=clemail:cli
    ''',
)