from app import app
from flask import Session

if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    Session.init_app(app)
    app.debug = True
    app.run()

