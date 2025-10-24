from setuptools import setup, find_packages

setup(
    name='django-security-headers',
    version='0.1.0',
    packages=find_packages(),
    description='Automatic security headers middleware for Django',
    install_requires=['django'],
)
