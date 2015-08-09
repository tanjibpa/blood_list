from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from project.search.views import search_blueprint
from project.users.views import users_blueprint

# register search blueprint
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)
