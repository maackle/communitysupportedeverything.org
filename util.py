import re
from unicodedata import normalize
from flask import make_response, send_file
from gridfs import GridFS
from gridfs.errors import NoFile
from bson.objectid import ObjectId

from pymongo import MongoClient

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def getFS(db):
	if not FS:
		FS = GridFS(db)
	return FS

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

def gridfs_response(file):
	try:
		data = file.read()
		res = make_response(data)
		res.mimetype = file.content_type
		return res
	except NoFile:
		abort(404)


def gridfs_response_raw(data, content_type):
	try:
		res = send_file(data, mimetype=content_type)
		return res
	except NoFile:
		abort(404)
