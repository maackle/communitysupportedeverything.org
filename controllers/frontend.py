import requests

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.ext.login import current_user, login_required
from mongoengine.errors import NotUniqueError


blueprint = Blueprint('frontend', __name__, template_folder='templates')

@blueprint.route('/')
def home():
	return render_template('views/frontend/home.jade')


@blueprint.route('/html')
def home_html():
	return render_template('views/home.html')

# @blueprint.route('/update-photo', methods='POST'):

