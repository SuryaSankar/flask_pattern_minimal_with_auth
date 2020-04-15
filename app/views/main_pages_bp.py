from flask import Blueprint, render_template

main_pages_bp = Blueprint('main_pages_bp', __name__)


@main_pages_bp.route("/")
def index():
    return render_template("index.html")


@main_pages_bp.route("/about")
def about():
    return render_template("about.html")