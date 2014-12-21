import re
import urllib

class AWSStatusPage(object):
    """
    This class wraps access to Amazon status page and can be used to retrieve
    all available RSS feeds, and through these feeds monitored regions and
    services.
    It may be used to automatically discover new available feeds for instance,
    or for checking regions/services list.
    """
    BASE_URL = 'http://status.aws.amazon.com/'
    RSS_RE = r'href="(?P<feed_url>rss/(?P<feed_name>[^"]+)\.rss)"'

    def __init__(self):
        self.page_source = None
        self.rss_urls = set()
        self.services = set()
        self.regions = set()
        self.parse_page()

    def page(self):
        if not self.page_source:
            self.page_source = urllib.urlopen(self.BASE_URL)
        return self.page_source

    def extract_elements(self, feed_name):
        service = region = None
        #general case: a normal region at the end
        #ex: cloudfront-us-east-1
        #special case: pseudo-region "us-standard"
        #ex: s3-us-standard
        match = re.search(r'(.*)-(\w+-\w+-\d|us-standard)$', feed_name)
        if match:
            service = match.group(1)
            region = match.group(2)
        #special case: services with no region
        #ex: route53, or management-console
        else:
            service = feed_name

        return [service, region]

    def parse_page(self):
        page_content = self.page().read()
        for match in re.finditer(self.RSS_RE, page_content):
            self.rss_urls.add( self.BASE_URL + match.group('feed_url') )
            service, region = self.extract_elements(match.group('feed_name'))
            if service:
                self.services.add(service)
            if region:
                self.regions.add(region)

