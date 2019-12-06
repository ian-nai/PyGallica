from setuptools import setup

setup(
    name = 'pygallica',
    packages = ['pygallica_api'], 
    version = '0.1',
    description = 'A Python client for the Gallica API',
    author = 'Ian Goodale',
    author_email = 'ianpgoodale@gmail.com',
    url = 'https://github.com/ian-nai',   
    download_url = 'https://github.com/ian-nai/PyGallica/archive/master.tar.gz',
    keywords = ['libraries', 'library', 'Gallica', 'France'],
    test_suite = 'tests',
    classifiers = [],
    install_requires = [ 'requests', 'beautifulsoup4', 'lxml', 'xmltodict' ]
)

