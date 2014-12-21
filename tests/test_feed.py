import unittest

from aws_status import Feed

class TestFeed(unittest.TestCase):
    def test_service_and_region_extraction(self):
        feed = Feed("https://amazon.status.page/rss/service-us-east-1.rss")
        self.assertEqual(feed.service, "service")
        self.assertEqual(feed.region, "us-east-1")
        feed = Feed("https://amazon.status.page/rss/this-is-a-service-us-standard.rss")
        self.assertEqual(feed.service, "this-is-a-service")
        self.assertEqual(feed.region, "us-standard")

    def test_service_and_region_extraction_special_case(self):
        feed = Feed("https://amazon.status.page/rss/this-is-a-service-with-no-region.rss")
        self.assertEqual(feed.service, "this-is-a-service-with-no-region")
        self.assertEqual(feed.region, None)
