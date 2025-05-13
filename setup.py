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
        'pybt',
        'pybt.api',
        'pybt.core',
        'examples'
    ],
    url=__url__,
    install_requires=[
        'requests>=2.31.0',
        'python-dotenv>=1.0.0',
    ],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
