import re
import sys
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.ext.login import current_user, login_required
from mongoengine.errors import NotUniqueError


from cache import cache
from decorators import project_required
from util import gridfs_response, gridfs_response_raw

blueprint = Blueprint('project', __name__, template_folder='templates')

@blueprint.route('/')
def home():
	return "project"


@blueprint.route('/<project_slug>/image/')
@blueprint.route('/<project_slug>/image/<size>/')
@project_required
# @cache.memoize(50)
def image(project, size=None, **kwargs):
	from PIL import Image
	import StringIO

	if size:
		m = re.match(r'([^x]+)(x([^x]+))?', size)
		if m.group(3):
			dims = (int(m.group(1)), int(m.group(3)))
		elif m.group(1):
			dims = (int(m.group(1)), int(m.group(1)))
		else:
			raise Exception("Bad dimensions")
		data = StringIO.StringIO()
		data.write(project.image.read())
		data.seek(0)
		im = Image.open(data)
		im.thumbnail(dims)
		data = StringIO.StringIO()
		im.save(data, 'PNG')
		data.seek(0)
		return gridfs_response_raw(data, project.image.content_type)
	else:
		return gridfs_response(project.image)
	# return gridfs_response(project.image)


@blueprint.route('/<project_slug>/overview/')
@project_required
def overview(project):
	return render_template('views/project/overview.jade', project=project)