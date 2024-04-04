from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 2 - Early Release',
    'Intended Audience :: Software Developers',
    'Operating System :: Linux :: Windows',
    'License :: OSI approved :: CC0',
    'Programming Language :: Python :: 3'
]

setup(
    name='Carot',
    version='0.5',
    description='this is a simple library to help with backend development',
    long_description='this is a simple library to help with backend development',
    url='',
    author='Mattis Leif Emanuel Kardell',
    author_email='kardellmattis@gmail.com',
    license='GNU AGPLv3',
    classifiers=classifiers,
    keywords='Backend Development, Networking, Database programming',
    packages=find_packages()
)
