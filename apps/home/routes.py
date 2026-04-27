# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from functools import wraps


# Custom decorators for role-based access
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('authentication_blueprint.login'))
        if current_user.role not in ['admin', 'developer']:
            return render_template('home/page-403.html'), 403
        return f(*args, **kwargs)
    return decorated_function


def cashier_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('authentication_blueprint.login'))
        if current_user.role not in ['cashier', 'admin', 'developer']:
            return render_template('home/page-403.html'), 403
        return f(*args, **kwargs)
    return decorated_function


def developer_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('authentication_blueprint.login'))
        if current_user.role != 'developer':
            return render_template('home/page-403.html'), 403
        return f(*args, **kwargs)
    return decorated_function


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index', user=current_user)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        segment = get_segment(request)

        return render_template("home/" + template, segment=segment, user=current_user)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
