#!/usr/bin/env python2.7
import os
from config import client_id, client_secret, mysql_credentials, redirect_uri

from flask import Flask, redirect, request, session
from requests_oauthlib import OAuth2Session

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)


# This information is obtained upon registration of a new GitHub OAuth
# application here: https://github.com/settings/applications/new


authorization_base_url = 'https://www.twitchalerts.com/api/v1.0/authorize'
token_url = 'https://www.twitchalerts.com/api/v1.0/token'
scope = ["donations.read", "donations.create"]


@app.route("/twitchalerts/authorize")
def authorize():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    twitchalerts = OAuth2Session(
        client_id, scope=scope, redirect_uri=redirect_uri)
    authorization_url, state = twitchalerts.authorization_url(
        authorization_base_url)
    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/twitchalerts/authorized", methods=["GET", "POST"])
def authorized():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    code = request.args.get('code', '')
    twitchalerts = OAuth2Session(
        client_id, redirect_uri=redirect_uri)  # state=session['oauth_state']
    token = twitchalerts.fetch_token(
        token_url, client_secret=client_secret, code=code)
    """ Here is an example of cURL snippet for obtaining an access_token
    This will pass everything as Form Data
    curl  \
        -X POST -F 'grant_type=authorization_code' -F 'client_id=YOUR_CLIENT_ID' -F 'client_secret=YOUR_CLIENT_SECRET' -F 'redirect_uri=YOUR_REDIRECT_URI' -F  'code=YOUR_CODE' \
        https://www.twitchalerts.com/api/v1.0/token
    """
    params = {'access_token': token['access_token'], 'limit': 100}
    data = twitchalerts.get(
        'https://www.twitchalerts.com/api/v1.0/donations', params=params)
    print(data)
    return str(token["access_token"])


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['DEBUG'] = "1"
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8080)
