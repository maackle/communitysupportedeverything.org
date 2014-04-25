from flask.ext.login import UserMixin
from flask.ext.mongoengine import Document
from mongoengine import *


class Profile(EmbeddedDocument):

	name = StringField(max_length=128, required=True)


class Project(Document):
	
	name = StringField(max_length=128, required=True)
	owner = ReferenceField('User')


class User(Document, UserMixin):

	email = StringField(max_length=128, required=True)
	password = StringField(max_length=128, required=True)
	profile = EmbeddedDocumentField(Profile)
	projects = ListField(ReferenceField(Project))

	def get_id(self):
		return str(self.id)

	@staticmethod
	def authenticate(email, password):
		user = User.objects(email=email, password=password).first()
		return user
