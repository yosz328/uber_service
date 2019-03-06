# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.estimated_time import EstimatedTime  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUberController(BaseTestCase):
    """UberController integration test stubs"""

    def test_get_time_post(self):
        """Test case for get_time_post

        obtener tiempo estimado con las locaciones
        """
        body = EstimatedTime()
        response = self.client.open(
            '/v2/get_time',
            method='POST',
            data=json.dumps(body),
            content_type='application/json ')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
