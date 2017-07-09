# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic
uld now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

$ heroku login
$ git clone folder.git
$ cd folder
$ heroku create (when u create an app, a git remote called heroku is also created and associated with your local git repository)
$ git push heroku master
$ heroku ps:scale web=1(等于0则不能访问)
$ heroku open
$ heroku logs --tail
$ heroku ps
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py collectstatic
$ heroku local web -f Procfile.windows

$ git add .
$ git commit -m "commit"
$ git push heroku master

$ heroku addons
$ heroku addons:create papertrail
$ heroku addons:open papertrail

$ heroku run python manage.py shell
$ heroku run bash

$ heroku congif
$ heroku config:set TIMES=2

$ heroku pg
$ heroku run python manage.py migrate
$ heroku pg:psql

$ heroku apps:rename newname
$ heroku apps:rename newname --app oldname
$ git remote rm heroku
$ heroku git:remote -a newname

free dyno hours: $ heroku ps -a <app_name>


https://devcenter.heroku.com/articles/getting-started-with-python#introduction
