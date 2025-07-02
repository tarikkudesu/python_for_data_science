"""
    build the ft_package using the lagacy setup.py way
"""

from setuptools import setup, find_packages


setup(
    name="ft_package",
    version='0.0.1',
    author="eagle",
    author_email="eagle@42.fr",
    description='A sample test package',
    url="https://github.com/eagle/ft_package",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    license="MIT"
)
