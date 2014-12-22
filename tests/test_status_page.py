import subprocess
import unittest

from aws_status.status_page import StatusPage

class TestStatusPage(unittest.TestCase):
    def test_number_of_detected_feeds(self):
        command = "curl -s http://status.aws.amazon.com/|grep rss|sort -u|wc -l"
        p = subprocess.Popen(command, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      shell=True)
        output, errors = p.communicate()
        expected_feeds = int(output)
        self.assertEqual(expected_feeds, len(StatusPage().rss_urls))

    def test_exposes_feeds(self):
        self.assertIsInstance(StatusPage().feeds, type(set()))
