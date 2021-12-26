import setuptools
from pybt import __version__, __url__, __author__, __author_email__, __license__, __description__

with open("docs/source/README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='bt-python-sdk',
    version=__version__,
    description=__description__,
    long_description=long_description,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    packages=[
        'examples',
        'examples.system',
        'pybt'
        ],
    url=__url__,
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
