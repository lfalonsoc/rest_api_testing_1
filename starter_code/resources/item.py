from typing import Any

from flask_restful import Resource, reqparse
from sqlalchemy import exc

from starter_code.models.item import ItemModel


class Item(Resource):
    parser: Any = reqparse.RequestParser()
    help: str = "This field cannot be left blank!"
    parser.add_argument(
        "price", type=float, required=True, help=help
    )

    def get(self, name: str) -> Any:
        item: Any = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name: str) -> Any:
        if ItemModel.find_by_name(name):
            return {
                "message": f"An item with name '{name}' already exists."
            }, 400

        data: Any = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except exc.SQLAlchemyError:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name: str) -> dict[str, str]:
        item: Any = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message": "Item deleted"}

    def put(self, name: str) -> dict[str, Any] | Any | None:
        data: Any = Item.parser.parse_args()

        item: Any = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]

        item.save_to_db()

        return item.json()
