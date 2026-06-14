# -*- encoding: utf-8 -*-
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
import os
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def seed_users():
    from apps.authentication.models import Users
    seed = [
        {'username': 'dev',     'email': 'dev@electrostock.com',
            'password': 'dev123',     'role': 'developer'},
        {'username': 'admin',   'email': 'admin@electrostock.com',
            'password': 'admin123',   'role': 'admin'},
        {'username': 'cashier', 'email': 'cashier@electrostock.com',
            'password': 'cashier123', 'role': 'cashier'},
    ]
    for s in seed:
        if not Users.query.filter_by(username=s['username']).first():
            u = Users(username=s['username'], email=s['email'], role=s['role'])
            u.set_password(s['password'])
            db.session.add(u)
    db.session.commit()
    print('✅ Users seeded!')


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        try:
            db.create_all()
            seed_users()
        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e))
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                os.path.join(basedir, 'db.sqlite3')
            print('> Fallback to SQLite ')
            db.create_all()
            seed_users()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app
