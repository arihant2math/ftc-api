from setuptools import setup

setup(
    name='ftc_api',
    author='Ashwin Naren',
    author_email='arihant2math@gmail.com',
    license='MIT',
    description='A python client to access the FIRST Tech Challenge API',
    version='0.0.0',
    install_requires=[
        'httpx', 'attrs', 'python-dateutil'
    ],
)
