from setuptools import setup

setup(
    name='Image Finder',
    version='1.0.0',
    py_modules = ['cli'],
    install_requires=['BeautifulSoup4','Click','selenium',],
    entry_points = '''
    [console_scripts]
    cli=cli:main
    '''
)