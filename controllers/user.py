import requests

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.ext.login import current_user, login_required
from mongoengine.errors import NotUniqueError

from forms import UserProfileForm
from models import User


blueprint = Blueprint('user', __name__, template_folder='templates')

@login_required
@blueprint.route('/')
def home():
	users = User.objects()
	return render_template('views/user/home.jade', users=users)

@login_required
@blueprint.route('/<user_id>/profile')
def profile(user_id):
	user = User.objects(id=user_id).first()
	form = UserProfileForm()
	return render_template('views/user/profile.jade', user=user, form=form)
