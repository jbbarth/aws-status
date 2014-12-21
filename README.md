aws-status
==========

[![Build Status](https://travis-ci.org/jbbarth/aws-status.svg?branch=master)](https://travis-ci.org/jbbarth/aws-status)

Helps you check AWS status as seen from the official status page http://status.aws.amazon.com/

Installation
------------

It is recommended to install the package through pip:
```
pip install aws-status
```

Usage
-----

The package provides 2 scripts, one for listing AWS available feeds (or regions or services):
```
#list feeds
aws-status-list

#list regions
aws-status-list --regions

#list services
aws-status-list --services

#get some help
aws-status-list --help
```

And an other one to check the status of a specific feed:
```
#check EC2 in us-east-1
aws-status-check http://status.aws.amazon.com/rss/ec2-us-east-2.rss
```

Thanks
------

- a great article about packaging python apps: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
- one example of parsing AWS status feeds (in Python): https://github.com/rhartkopf/check_aws_status_feed/blob/master/check_aws_status_feed.py
- an other example (in Ruby): https://gist.github.com/ktheory/1604786
