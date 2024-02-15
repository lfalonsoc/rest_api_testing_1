from starter_code.models.item import ItemModel
from starter_code.tests.unit.test_db import TestDB


class TestItem(TestDB):
    def test_crud(self) -> None:
        with self.app_context():
            item: ItemModel = ItemModel("test", 19.99)
            self.assertIsNone(ItemModel.find_by_name("test"))

            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name("test"))

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name("test"))
