"""
TestBase

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from typing import Any
from unittest import TestCase

from starter_code.app import app
from starter_code.db import db


class TestDB(TestCase):
    def setUp(self) -> None:
        # Make suere database exist
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app: Any = app.test_client()
        self.app_context: Any = app.app_context

    def tearDown(self) -> None:
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
