import feedparser
import re


STATUS_OK = 0
STATUS_WARNING = 1
STATUS_CRITICAL = 2
STATUS_UNKNOWN = 3


def get_status(title, description):
    if title.startswith("Service is operating normally") \
       or '[RESOLVED]' in title \
       or '[Resolved]' in title \
       or re.search("he service is (now )?operating normally.?\n?", description) \
       or title.startswith("OK"):
        status = STATUS_OK
    elif title.startswith("Informational message") or title.startswith("Performance issues"):
        status = STATUS_WARNING
    elif title.startswith("Service disruption"):
        status = STATUS_CRITICAL
    else:
        status = STATUS_UNKNOWN
    return status


class Feed(object):
    """
    This class wraps informations about a given AWS status feed, e.g. its
    URL, the monitored service, the region, etc.
    """
    def __init__(self, feed_url):
        self.url = feed_url
        self.__extract_elements()

    def __extract_elements(self):
        self.service = self.region = None
        feed_name = re.sub(r'.*/([^/]+?)\.rss', r'\1', self.url)
        #general case: a normal region at the end
        #ex: cloudfront-us-east-1
        #special case: pseudo-region "us-standard"
        #ex: s3-us-standard
        match = re.search(r'(.*)-(\w+-\w+-\d|us-standard)$', feed_name)
        if match:
            self.service = match.group(1)
            self.region = match.group(2)
        #special case: services with no region
        #ex: route53, or management-console
        else:
            self.service = feed_name

    def status(self):
        try:
            parsed = feedparser.parse(self.url)
            if parsed.entries:
                return parsed.entries[0]
            elif parsed['feed']['title']:
                return { "title": "OK but no event to display (empty feed)" }
        except KeyError:
            return { "title": "Unknown status, unable to parse feed ("+self.url+")" }
