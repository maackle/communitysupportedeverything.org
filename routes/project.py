
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.ext.login import current_user, login_required
from mongoengine.errors import NotUniqueError

from decorators import project_required
from util import gridfs_response

blueprint = Blueprint('project', __name__, template_folder='templates')

@blueprint.route('/')
def home():
	return "project"


@blueprint.route('/<project_slug>/image/')
@project_required
def image(project, **kwargs):
	return gridfs_response(project.image)


@blueprint.route('/<project_slug>/overview/')
@project_required
def overview(project):
	render_template('views/project/overview.html', project=project)