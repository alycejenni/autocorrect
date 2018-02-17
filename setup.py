from setuptools import setup, find_packages

setup(
    name='autocorrect',
    version='0.1',
    packages=find_packages(),
    package_data={'autocorrect': ['data/autocorrect.json']},
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
