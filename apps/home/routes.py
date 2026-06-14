# -*- encoding: utf-8 -*-
from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from functools import wraps
from apps import db


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('authentication_blueprint.login'))
        if current_user.role not in ['admin', 'developer']:
            return render_template('home/page-403.html'), 403
        return f(*args, **kwargs)
    return decorated_function


@blueprint.route('/index')
@login_required
def index():
    from apps.authentication.models import Product
    total_products = Product.query.filter_by(is_active=True).count()
    low_stock = Product.query.filter(
        Product.stock_qty <= Product.low_stock_threshold,
        Product.is_active == True
    ).count()
    return render_template('home/index.html',
                           segment='index',
                           total_products=total_products,
                           low_stock=low_stock,
                           today_sales=0,
                           total_customers=0)


@blueprint.route('/products')
@login_required
@admin_required
def products():
    from apps.authentication.models import Product
    all_products = Product.query.filter_by(
        is_active=True).order_by(Product.created_at.desc()).all()
    return render_template('home/products.html', segment='products', products=all_products)


@blueprint.route('/products/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_product():
    from apps.authentication.models import Product
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description')
        price = float(request.form.get('price', 0))
        stock_qty = int(request.form.get('stock_qty', 0))
        low_stock_threshold = int(request.form.get('low_stock_threshold', 10))

        product = Product(
            name=name,
            category=category,
            description=description,
            price=price,
            stock_qty=stock_qty,
            low_stock_threshold=low_stock_threshold
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('home_blueprint.products'))

    return render_template('home/add_product.html', segment='products')


@blueprint.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_product(product_id):
    from apps.authentication.models import Product
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.category = request.form.get('category')
        product.description = request.form.get('description')
        product.price = float(request.form.get('price', 0))
        product.stock_qty = int(request.form.get('stock_qty', 0))
        product.low_stock_threshold = int(
            request.form.get('low_stock_threshold', 10))
        db.session.commit()
        return redirect(url_for('home_blueprint.products'))

    return render_template('home/edit_product.html', segment='products', product=product)


@blueprint.route('/products/delete/<int:product_id>')
@login_required
@admin_required
def delete_product(product_id):
    from apps.authentication.models import Product
    product = Product.query.get_or_404(product_id)
    product.is_active = False
    db.session.commit()
    return redirect(url_for('home_blueprint.products'))


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        segment = get_segment(request)
        return render_template("home/" + template, segment=segment)
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500


def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None
