# package and distribution management

from setuptools import setup
setup(
    name = 'imdbsearch',
    version = '1.0',
    packages = ['imdbsearch'],
    entry_points = {
        'console_scripts': [
            'imdbsearch = imdbsearch.__main__:main'
        ]
    },
    install_requires=['beautifulsoup4', 'requests']
)