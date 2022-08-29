from distutils.core import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='moydomjkh',
    packages=['moydomjkh'],
    version='0.0.2',
    license='MIT',
    description='api для работы с порталом https://newlk.erconline.ru/',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='@yusinv',
    author_email='yusinv@gmail.com',
    url='https://github.com/yusinv/moydomjkh',
    keywords=['moydomjkh'],
    install_requires=[
        'requests',
        'argparse'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': ['moydomjkh=moydomjkh.command_line:main'],
    }
)
