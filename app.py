#!/usr/bin/env python3

import connexion
from database.base import db_session

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Animal Pet'})
    app.run(port=5000)

application = app.app

@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
