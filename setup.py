from setuptools import setup, find_packages

from indexdigest import VERSION

# @see https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py
with open("README.md", "r") as fh:
    long_description = fh.read()

# @see https://github.com/pypa/sampleproject/blob/master/setup.py
setup(
    name='indexdigest',
    version=VERSION,
    author='Maciej Brencz',
    author_email='maciej.brencz@gmail.com',
    license='MIT',
    description='Analyses your database queries and schema and suggests indices and schema improvements',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/macbre/index-digest',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Database',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    extras_require={
        'dev': [
            'coverage==5.2',
            'pylint>=2.4.2',
            'pytest==5.2.0',
            'twine==2.0.0',
        ]
    },
    install_requires=[
        'docopt==0.6.2',
        'PyYAML==5.1.2',
        'mysqlclient==2.0.1',
        'sql_metadata==1.5.0',
        'termcolor==1.1.0',
        'yamlordereddictloader==0.4.0'
    ],
    entry_points={
        'console_scripts': [
            'add_linter=indexdigest.cli.add_linter:main',  # creates a new linter from a template
            'index_digest=indexdigest.cli.script:main',
        ],
    }
)
