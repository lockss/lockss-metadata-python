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
from lockss_metadata.api.metadata_api import MetadataApi  # noqa: E501
from lockss_metadata.rest import ApiException


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = lockss_metadata.api.metadata_api.MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_metadata_aus_auid(self):
        """Test case for delete_metadata_aus_auid

        Delete the metadata stored for an AU  # noqa: E501
        """
        pass

    def test_get_metadata_aus_auid(self):
        """Test case for get_metadata_aus_auid

        Get the metadata stored for an AU  # noqa: E501
        """
        pass

    def test_post_metadata_aus_item(self):
        """Test case for post_metadata_aus_item

        Store the metadata for an AU item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
