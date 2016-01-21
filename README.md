# Twitchalerts OAuth Handler

Everyone knows OAuth is a pain. Here is a little something to ease your suffering.

## Installation

### Virtual Environment

I would recommend running this in a virtual environment to keep your
dependencies in check. If you'd like to do that, run:

`sudo pip install virtualenv`

Followed by:

`virtualenv venv`

This will create an empty virtualenv in your project directory in a folder
called "venv." To enable it, run:

`source venv/bin/activate`

and your console window will be in that virtualenv state. To deactivate, run:

`deactivate`

### Dependencies

To install all dependencies locally (preferably inside your activated
virtualenv), run:

`pip install -r requirements.txt`

### Further Steps

Make a copy of the example config file:

`cp config_example.py config.py`

Then modify your twitchalerts app's info to reflect your registered app.
Make sure to bookmark the page for your twitchalerts app so you don't lose this
information. To register an app, go to:

http://twitchalerts.com/oauth/apps/register

And have their documentation open as a resource:

https://twitchalerts.readme.io/docs/getting-started

For testing, I recommend setting your `redirect_uri` to something like:

http://127.0.0.1:8080/twitchalerts/authorized

Make sure this matches in your TwitchAlerts app settings and in `config.py`!

## Finally

### To run:

`./app.py`

## Authorization

Head to http://127.0.0.1:8080/twitchalerts/authorize to see an authorization page for
the app.

From their, once approved, you'll see a returned access token, assuming all the
provided information from your app (and the `redirect_uri`) are correct.
