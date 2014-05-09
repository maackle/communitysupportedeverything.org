from flask.ext.login import UserMixin
from flask.ext.mongoengine import Document
from mongoengine import *
from mongoengine import signals

from util import slugify

from application import db

class Project(db.Document):

	def __unicode__(self):
		return self.name
	
	name = db.StringField(max_length=128, required=True)
	image = db.ImageField(size=(1024, 1024))
	slug = db.StringField(max_length=128, required=True, unique=True)
	excerpt = db.StringField(max_length=4096)
	content = db.StringField(max_length=8192)

	@classmethod
	def pre_save(cls, sender, document, **kwargs):
		document.slug = slugify(document.name)


class Profile(db.EmbeddedDocument):

	meta = {'allow_inheritance': True}
	full_name = db.StringField(max_length=128, required=True)


class ResidentProfile(Profile):

	# TODO: inherit from Profile.

	# full_name = db.StringField(max_length=128, required=True)
	short_bio = db.StringField(max_length=2048)
	bio = db.StringField(max_length=8192)
	image = db.ImageField(size=(1024, 1024))

	projects = db.ListField(db.ReferenceField(Project))


class User(db.Document, UserMixin):

	def __unicode__(self):
		return self.profile.full_name

	meta = {
		'allow_inheritance': True,
		'indexes': ['id', 'slug',],
	}

	email = db.StringField(max_length=128, required=True)
	password = db.StringField(max_length=128, required=True)

	slug = db.StringField(max_length=128, required=True)
	
	profile = db.EmbeddedDocumentField(Profile)


	def get_id(self):
		return str(self.id)

	@staticmethod
	def authenticate(email, password):
		user = User.objects(email=email, password=password).first()
		return user

	@classmethod
	def pre_save(cls, sender, document, **kwargs):
		document.slug = slugify(document.profile.full_name)
		document.email = document.email.lower()


class Resident(User):

	profile = db.EmbeddedDocumentField(ResidentProfile)


signals.pre_save.connect(User.pre_save, sender=User)
signals.pre_save.connect(Resident.pre_save, sender=Resident)
signals.pre_save.connect(Project.pre_save, sender=Project)