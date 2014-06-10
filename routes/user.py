import requests

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.ext.login import current_user, login_required
from mongoengine.errors import NotUniqueError

from forms import ResidentProfileForm
import models
from models import User
from decorators import user_required, owner_required
from util import gridfs_response

blueprint = Blueprint('user', __name__, template_folder='templates')

@blueprint.route('/')
def home():
	users = User.objects()
	return render_template('views/user/home.jade', users=users)

# @login_required
@blueprint.route('/<user_slug>/')
@user_required
def profile(user, **kwargs):
	# user = kwargs['user']
	# user = User.objects(slug=user_slug).first()
	return render_template('views/user/profile_view.jade', user=user)


@blueprint.route('/<user_slug>/image/')
@user_required
def image(user, **kwargs):
	return gridfs_response(user.profile.image)

@blueprint.route('/<user_slug>/profile/image/')
@user_required
def profile_image(user, **kwargs):
	return gridfs_response(user.profile.background_image)


@blueprint.route('/<user_slug>/edit/', methods=['GET', 'POST',])
@owner_required
def profile_edit(user):

	# if not user.profile:
	# 	user.profile = models.Profile()
	form = ResidentProfileForm(obj=user.profile)
	template = 'views/user/profile_edit.jade'
	if request.method == 'GET':
		return render_template(template, user=user, form=form)
	else:
		if form.validate():
			form.populate_obj(user.profile)
			user.save()
			flash('Profile updated', 'success')
			return redirect(url_for('.profile_edit', user_slug=user.slug))
		else:
			print(form.errors)
			flash('Problem updating profile.', 'danger')
			return render_template(template, user=user, form=form)

