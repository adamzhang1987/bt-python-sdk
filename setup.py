import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='bt-python-sdk',
    version='0.1.0',
    description='Pybt is a BaoTa panel python sdk.',
    long_description=long_description,
    author='Adam Zhang',
    author_email='adamzhang1987@gmail.com',
    license='MIT',
    packages=[
        'examples',
        'examples.system',
        'pybt'
        ],
    url='https://github.com/adamzhang1987/python-bt-sdk',
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
