#!/bin/bash
set -e
version_file=aws_status/__init__.py
echo "Current version: $(grep __version__ $version_file)"
echo -n "What is the new version number? : "
read version
perl -pi -e "s/^__version__.*/__version__ = '$version'/" $version_file
git commit -a -m "Bump version to $version"
git tag $version
git push
git push --tags
python setup.py sdist upload -r pypi
