import os

from setuptools import setup, find_packages

version = __import__('aws_status').__version__

def read(path):
    """Return the content of a file."""
    with open(path, 'r') as f:
        return f.read()

setup(
    name='aws-status',
    version=version,
    description='Wraps AWS status informations obtained via the status page.',
    long_description=(read('README.rst')),
    url='http://github.com/jbbarth/aws-status',
    license='MIT',
    author='Jean-Baptiste Barth',
    author_email='jeanbaptiste.barth@gmail.com',
    packages=find_packages(exclude=['tests*']),
    scripts=[
        'bin/aws-status-check',
        'bin/aws-status-list',
    ],
    install_requires=[
        'feedparser>=5.1.3',
    ],
    include_package_data=True,
    #see http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
    ],
)
