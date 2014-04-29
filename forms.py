from flask.ext.wtf import Form
from flask.ext.wtf.file import FileField
from flask.ext.mongoengine.wtf import model_form
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, HiddenField, FieldList, IntegerField
from wtforms import widgets
from wtforms.validators import Length, EqualTo, InputRequired, Optional, ValidationError, URL

from models import User, ResidentProfile

required = InputRequired("This field is required")

##################################################

LoginForm = model_form(User, Form, only=('email', 'password',))

RegisterForm = model_form(User, Form, only=('email', 'password', 'profile'))

UserSettingsForm = model_form(User, Form, exclude=('slug', 'profile',))

ProfileForm = model_form(ResidentProfile, Form)

class ResidentProfileFormBase(Form):

	image = FileField("Photograph", [required,])

ResidentProfileForm = model_form(ResidentProfile, ResidentProfileFormBase, only=('full_name', 'image', 'short_bio'), field_args = {
	'short_bio': {
		'widget': widgets.TextArea()
	}
})