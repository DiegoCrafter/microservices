# services/users/project/__init__.py
import os  # nuevo
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # nuevo
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate
<<<<<<< HEAD
from flask_bcrypt import Bcrypt
# instanciado la app
app = Flask(__name__)


=======
# instanciado la app
app = Flask(__name__)

# establecer configuraicon
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
app_settings = os.getenv('APP_SETTINGS')   # Nuevo
app.config.from_object(app_settings)       # Nuevo

# instanciando la db
db = SQLAlchemy(app)  # nuevo
toolbar = DebugToolbarExtension()
cors = CORS()
migrate = Migrate()
<<<<<<< HEAD
bcrypt = Bcrypt()
=======
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1


def create_app(script_info=None):
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
<<<<<<< HEAD
    bcrypt.init_app(app)
=======
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app
