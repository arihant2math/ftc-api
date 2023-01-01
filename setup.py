from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ftc_api',
    author='Ashwin Naren',
    author_email='arihant2math@gmail.com',
    license='MIT',
    description='A python client to access the FIRST Tech Challenge API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0',
    install_requires=[
        'httpx', 'attrs', 'python-dateutil'
    ]
)
