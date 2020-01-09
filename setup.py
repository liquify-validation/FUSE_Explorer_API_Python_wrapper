import setuptools

setuptools.setup(
    name='Fuse_Explorer_API',
    version='1.0',
    packages=['Fuse_Explorer_API'],
    url='https://github.com/Andrew-Pohl/FUSE_Explorer_API_Python_wrapper',
    license='MIT',
    author='Andy Pohl',
    author_email='andypohl@hotmail.co.uk',
    description='Python wrapper for the FUSE explorer api',
    install_requires=[
        'requests>=2.21.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)