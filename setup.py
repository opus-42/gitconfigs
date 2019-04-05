from setuptools import setup, find_packages

setup(
    name="gitconfigs",
    version="0.1",
    packages=find_packages(),
    scripts=[],
    install_requires=[
        'click>=7.0'
    ],
    author="Emmanuel Bavoux",
    author_email="emmanuel.bavoux@gmail.com",
    description="Some description")
