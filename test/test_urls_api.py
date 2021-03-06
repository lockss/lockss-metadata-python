# coding: utf-8

"""
    LOCKSS Metadata Service REST API

    API of the LOCKSS Metadata REST Service  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: lockss-support@lockss.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import lockss_metadata
from lockss_metadata.api.urls_api import UrlsApi  # noqa: E501
from lockss_metadata.rest import ApiException


class TestUrlsApi(unittest.TestCase):
    """UrlsApi unit test stubs"""

    def setUp(self):
        self.api = lockss_metadata.api.urls_api.UrlsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_urls_doi(self):
        """Test case for get_urls_doi

        Gets the URL for a DOI  # noqa: E501
        """
        pass

    def test_get_urls_open_url(self):
        """Test case for get_urls_open_url

        Performs an OpenURL query  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
