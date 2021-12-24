import setuptools

setuptools.setup(
    name='pybt',
    version='0.1.0',
    description='Pybt is a BaoTa panel python sdk.',
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
        "Programming Language :: Python :: 3"
    ],
    include_package_data=True,
    zip_safe=False,
)
