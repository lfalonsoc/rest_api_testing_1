import os
from flask import Flask
from flask_restful import Api

from starter_code.resources.item import Item

app: Flask = Flask(__name__)

app.config['DEBUG'] = True

db_url: str = "DATABASE_URL"
name_db: str = "sqlite:///data.db"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(db_url, name_db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api: Api = Api(app)

api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables() -> None:
            db.create_all()

    app.run(port=5000)
