# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])




from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional, Length

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(max=128)])
    category = SelectField('Category', choices=[
        ('', 'Select Category'),
        ('Laptop', 'Laptop'),
        ('Desktop', 'Desktop'),
        ('Monitor', 'Monitor'),
        ('Keyboard', 'Keyboard'),
        ('Mouse', 'Mouse'),
        ('Printer', 'Printer'),
        ('Accessory', 'Accessory')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    price = FloatField('Selling Price', validators=[DataRequired(), NumberRange(min=0)])
    stock_qty = IntegerField('Stock Quantity', default=0, validators=[NumberRange(min=0)])
    low_stock_threshold = IntegerField('Low Stock Alert at', default=10, validators=[NumberRange(min=0)])
    image = StringField('Image URL', validators=[Optional(), Length(max=256)])
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save Product')