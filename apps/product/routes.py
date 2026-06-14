from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('product', __name__, url_prefix='/products')


@blueprint.route('/')
@login_required
def list_products():
    return "Products page works!"
