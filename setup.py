from setuptools import setup

setup(
    name='autocorrect',
    version='0.1',
    py_modules=['autocorrect'],
    package_data={'autocorrect': ['autocorrect/data/autocorrect.json']},
    include_package_data=True,
    install_requires=[
        'click',
        'redbaron'
        ],
    entry_points='''
        [console_scripts]
        autocorrect=autocorrect.cli:cli
    ''',
    )
