# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from datetime import datetime
from apps import db, login_manager
from apps.authentication.util import hash_pass


class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email    = db.Column(db.String(64), unique=True)
    password = db.Column(db.LargeBinary)
    role     = db.Column(db.String(20), default='cashier')

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]
            if property == 'password':
                value = hash_pass(value)
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

    def is_admin(self):
        return self.role == 'admin'

    def is_developer(self):
        return self.role == 'developer'

    def is_cashier(self):
        return self.role == 'cashier'


class Product(db.Model):

    __tablename__ = 'Products'

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(128), nullable=False)
    category    = db.Column(db.String(64))
    description = db.Column(db.Text)
    price       = db.Column(db.Float, nullable=False, default=0.0)
    stock_qty   = db.Column(db.Integer, default=0)
    low_stock_threshold = db.Column(db.Integer, default=10)
    image       = db.Column(db.String(256))
    is_active   = db.Column(db.Boolean, default=True)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return str(self.name)

    def is_low_stock(self):
        return self.stock_qty <= self.low_stock_threshold


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None