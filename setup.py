"""PyPublish : a tool to upload an audio file to Auphonic,
start the audio production, wait for production to complete,
download output files, upload those files to archive.org,
wait for files to be derived, and print out file URLs.
"""

# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyUpload',

    version='0.1.0',

    description='Automatically process audio file with Auphonic and upload the result to archive.org',
    long_description=long_description,

    url='https://github.com/ymauray/pyupload',

    author='The French Guy from Switzerland',
    author_email='yannick@frenchguy.ch',

    license='CC-BY-NC-SA 4.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Podcast publishers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='auphonic internetarchive audio podcast',

    py_modules=['pyupload'],

    entry_points={
        'console_scripts': [
            'pyupload=pyupload:main',
        ],
    },
)
