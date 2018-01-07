from setuptools import setup, find_packages

from indexdigest import VERSION

# @see https://github.com/pypa/sampleproject/blob/master/setup.py
setup(
    name='indexdigest',
    version=VERSION,
    author='Maciej Brencz',
    author_email='maciej.brencz@gmail.com',
    license='MIT',
    description='Analyses your database queries and schema and suggests indices improvements',
    url='https://github.com/macbre/index-digest',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Database',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    install_requires=[
        'docopt==0.6.2',
        'coverage==4.4.2',
        'pylint==1.8.1',
        'pytest==3.2.3',
        'PyYAML==3.12',
        'mysqlclient==1.3.12',
        'sqlparse==0.2.4',
        'termcolor==1.1.0',
        'yamlordereddictloader==0.4.0'
    ],
    entry_points={
        'console_scripts': [
            'index_digest=indexdigest.cli.script:main',
        ],
    }
)
