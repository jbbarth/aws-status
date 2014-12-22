import re
from urllib2 import urlopen
from .feed import Feed

class StatusPage(object):
    """
    This class wraps access to Amazon status page and can be used to retrieve
    all available RSS feeds, and through these feeds monitored regions and
    services.
    It may be used to automatically discover new available feeds for instance,
    or for checking regions/services list.
    """
    BASE_URL = 'http://status.aws.amazon.com/'
    RSS_RE = r'href="(?P<feed_url>rss/[^"]+\.rss)"'

    def __init__(self):
        self.page_source = None
        self.feeds = set()
        self.rss_urls = set()
        self.services = set()
        self.regions = set()
        self.parse_page()

    def page(self):
        if not self.page_source:
            self.page_source = urlopen(self.BASE_URL)
        return self.page_source

    def parse_page(self):
        page_content = self.page().read()
        for match in re.finditer(self.RSS_RE, page_content):
            absolute_url = self.BASE_URL + match.group('feed_url')
            feed = Feed(absolute_url)
            self.feeds.add(feed)
            self.rss_urls.add(feed.url)
            if feed.service:
                self.services.add(feed.service)
            if feed.region:
                self.regions.add(feed.region)

