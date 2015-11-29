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

### MySQL Installation

Depending on your distribution, starting the server will be different, on a mac,
this is accomplished by doing:

`brew install mysql`

`mysql.server start`

From here, you need to enter the mysql console as root:

`mysql -u root`

Create your database and name it whatever you want:

`CREATE DATABASE databasename;`

Create a user that you will use to connect with the database with (you do not
want to connect as root for security reasons) - replace "newuser" and
"password" with whatever you'd like:

`CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';`

Grant the appropriate privileges for your databases(s) to your new user:

`GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';`

Exit out of the console with:

`\q`

Create your schema from my blank template:

`mysql -u newuser -ppassword* databasename < schema.sql`

## Finally

### To run:

`./app.py`

## Authorization

Head to http://127.0.0.1:8080/authorize to see an authorization page for
the app.

From their, once approved, you'll see a returned access token, assuming all the
provided information from your app (and the uri redirect) are correct.

After you have this much, I'll leave it up to you to decide how you'll want
to store the tokens. I'm using MySQL here to interact with my own separate
application directly.
