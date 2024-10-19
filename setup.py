from setuptools import setup, find_packages

setup(
    name="simpleWebScraper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'selenium',
        'webdriver_manager',
        'requests',
    ],
)