"""Test flask.py module.

make test T=test_flask.py
"""
import os
from . import TestBase


class TestsFlask(TestBase):
    """Module flask.py."""

    def setUp(self):
        """Set up test data."""
        super(TestBase, self).setUp()
        from flask import Flask

        self.app = Flask(__name__)

    def test_bind(self):
        """Function bind."""
        from google_cloud_ndbm.flask import bind

        assert "GCLOUD_PROJECT" not in os.environ
        assert bind(self.app, "xxx")
        assert os.environ["GCLOUD_PROJECT"] == "xxx"
