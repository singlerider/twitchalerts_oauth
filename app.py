#!/usr/bin/env python2.7
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
from config import *
import os
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)


# This information is obtained upon registration of a new GitHub OAuth
# application here: https://github.com/settings/applications/new


authorization_base_url = 'https://www.twitchalerts.com/api/v1.0/authorize'
token_url = 'https://www.twitchalerts.com/api/v1.0/token'
scope = ["donations.read", "donations.create"]


@app.route("/authorize")
def demo():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    twitchalerts = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = twitchalerts.authorization_url(authorization_base_url)

    print "authorization_url: ", authorization_url, "state: ", state
    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/authorized", methods=["GET", "POST"])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    print request.args.get('code', '')
    code = request.args.get('code', '')
    twitchalerts = OAuth2Session(client_id, redirect_uri=redirect_uri) #state=session['oauth_state']
    token = twitchalerts.fetch_token(token_url, client_secret=client_secret, code=code)
    print token
    params = {'access_token': token['access_token'], 'limit':100 }
    d = twitchalerts.get('https://www.twitchalerts.com/api/v1.0/donations', params=params)
    print d.content
    print d

    #token = twitchalerts.fetch_token(token_url, refresh_token=refresh_token, client_secret=client_secret, code=code, grant_type='refresh_token')

    #access_token =
    return str(token["access_token"])


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['DEBUG'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8000)
