Community Supported Everything
==============================

This describes how to get the site up and running.

The site is built on [Flask](http://flask.pocoo.org/), a Python framework. [Grunt](http://gruntjs.com/) is also used for frontend development.

Server Setup
============

Set up virtualenv
-----------------

Install virtualenv to help with dependency management and versioning. Optionally install virtualenvwrapper to make the experience sexier.

### To create the virtualenv (do this only once:

With virtualenvwrapper:

	mkvirtualenv cse

With virtualenv only:

	virtualenv venv  # you can replace "venv" with anything

### To activate the virtualenv (do this every time you're starting to work):

With virtualenvwrapper:

	workon cse

With virtualenv only:

	source venv/bin/activate


Python dependencies
-------------------

After the virtualenv is activated (NOT before!), use:

	pip install -r requirements.txt

You can issue this command any time. This will download and install all necessary dependencies into the virtualenv you created.

If you need to install a new dependency yourself, via `pip install`, make sure you update the `requirements.txt`. You can do this easily with:

	pip freeze > requirements.txt

Then everyone else will have to `pip install -r requirements.txt` after pulling your change.

Running the server
------------------

	python server.py

Now you should have a server running at http://localhost:5005.

Running a local MongoDB instance (and using it)
-----------------------------------------------

By default the app connects to a remote MongoDB instance by default. To use a local instance, first make sure MongoDB is installed locally. You can run:

	mongod

in a new terminal window to start a development instance. Then, run the server from the command line like so:

	CSE_SETTINGS="config/development.py" python server.py

to use the development settings.


Frontend Setup
==============

We use Grunt to manage front-end build tasks.

Install NPM (Node Package Manager) if you don't have it. Then [install Grunt](http://gruntjs.com/getting-started).

To install all front-end dependencies:

	npm install

Then, every time you want to work on the front end, just run:

	grunt

Which will start a process that compiles LESS files, watches for changes, and runs LiveReload.


OK!
===

You should be all set up. Every time you want to work on the project, you'll want to run these two commands in two separate terminals:

	python server.py

and
	
	grunt

Develop away.


Deployment
==========

We are currently using Heroku for a dev server. To set up the git remote:

	git remote add git@heroku.com:community-supported-everything.git

To deploy, first ask us for collaborator access. Make sure you're on the git master branch, and simply:

	git push heroku

Boom shaka.