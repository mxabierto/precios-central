from setuptools import setup, find_packages
import precios


setup(
    name='precios',
    version='1.0.0'
    author='Francisco Vaquero',
    author_email='francisco@opi.la',
    packages=find_packages(),
    entrypoint={
        'console_scripts': [
            'precios=precio.cli.parse'
        ]
    }
)
