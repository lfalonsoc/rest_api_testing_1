from typing import Any
from unittest import TestCase

from starter_code.models.item import ItemModel


class TestItem(TestCase):
    def test_create_item(self) -> None:
        item: ItemModel = ItemModel("test", 19.99)
        msg_error: dict[str, str] = {
            "test": "Name item creation is diferent to the constructor.",
            "price": "Price item creation is diferent to the constructor.",
        }

        self.assertEqual(
            item.name, "test", msg_error["test"]
        )
        self.assertEqual(
            item.price, 19.99, msg_error["price"]
        )

    def test_item_json(self) -> None:
        item: ItemModel = ItemModel("test", 19.99)
        expected: dict[str, Any] = {"name": "test", "price": 19.99}
        msg_error: str = f"Json incorrect. rec {item.json()}, exp {expected}"

        self.assertEqual(
            item.json(), expected, msg_error
        )
