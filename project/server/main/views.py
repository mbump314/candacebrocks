# project/server/main/views.py

from flask_login import current_user
from flask import render_template, Blueprint


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():

    return render_template("main/home.html", current_user=current_user)


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
