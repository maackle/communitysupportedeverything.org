from functools import wraps

from flask import abort, redirect
from flask.ext.login import current_user

from models import User, Project

def user_required(f):
	'''
	Decorates any route function that takes a <user_slug> parameter.
	If a user with that slug exists, pass it on to the function as a <user> parameter instead.
	If not, throw 404.

	Useful for e.g. publicly available user views.
	'''

	@wraps(f)
	def decorated(*args, **kwargs):
		if 'user_slug' in kwargs:
			slug = kwargs['user_slug']
			user = User.objects(slug=slug).first_or_404()
		if user:
			del kwargs['user_slug']
			kwargs['user'] = user
			return f(*args, **kwargs)
		else:
			abort(404) 
	return decorated


def project_required(f):
	'''
	Decorates any route function that takes a <project_slug> parameter.
	If a project with that slug exists, pass it on to the function as a <project> parameter instead.
	If not, throw 404.

	Useful for e.g. publicly available project views.
	'''

	@wraps(f)
	def decorated(*args, **kwargs):
		if 'project_slug' in kwargs:
			slug = kwargs['project_slug']
			project = Project.objects(slug=slug).first_or_404()
		if project:
			del kwargs['project_slug']
			kwargs['project'] = project
			return f(*args, **kwargs)
		else:
			abort(404) 
	return decorated


def owner_required(f):
	'''
	Decorates any route function that takes a <user_slug> parameter.
	If a user with that slug exists, AND the current_user matches, pass it on to the function as a <user> parameter instead.
	If not, throw 404.

	Useful for e.g. letting a user manage his own settings.
	'''

	@wraps(f)
	def decorated(*args, **kwargs):
		if 'user_slug' in kwargs:
			slug = kwargs['user_slug']
			user = User.objects(slug=slug).first_or_404()
		if user and current_user.is_authenticated() and user.id == current_user.id:
			del kwargs['user_slug']
			kwargs['user'] = user
			return f(*args, **kwargs)
		else:
			abort(404) 
	return decorated

