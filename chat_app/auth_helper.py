import yaml
import msal
import os
import time

import requests
from rest_framework_jwt.utils import jwt_decode_handler

stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)

def load_cache(request):
  # Check for a token cache in the session
  cache = msal.SerializableTokenCache()
  if request.session.get('token_cache'):
    cache.deserialize(request.session['token_cache'])
  return cache

def save_cache(request, cache):
  # If cache has changed, persist back to session
  if cache.has_state_changed:
    request.session['token_cache'] = cache.serialize()

def get_msal_app ( cache=None ):
  # Initialize the MSAL confidential client
  auth_app = msal.ConfidentialClientApplication (
    settings['app_id'],
    client_credential = settings['app_secret'],
    # '300579e3-4a79-4fd2-8f09-60ed83326dd6',
    # 'kWe7Q~YiJxe0QOjZ-K.3hDUDfutYmzSucU1TA',
    authority = "https://login.microsoftonline.com/common",
    token_cache = cache
  )
  return auth_app

# Method to generate a sign-in flow
def get_sign_in_flow () :
  auth_app = get_msal_app()
  return auth_app.initiate_auth_code_flow (
    [],
    redirect_uri = settings['redirect'],
  )

# Method to exchange auth code for access token

def get_token_from_code(request):
  cache = load_cache(request)
  auth_app = get_msal_app(cache)

  # Get the flow saved in session
  flow = request.session.pop('auth_flow', {})
  result = auth_app.acquire_token_by_auth_code_flow(flow, request.GET)
  save_cache(request, cache)

  return result


def store_user(request, user):
  try:
    request.session['user'] = {
      'is_authenticated': True,
      'name': user['displayName'],
      'email': user['mail'] if (user['mail'] != None) else user['userPrincipalName'],
      'timeZone': user['mailboxSettings']['timeZone'] if (user['mailboxSettings']['timeZone'] != None) else 'UTC'
    }
  except Exception as e:
    print(e)

def get_token(request):
  cache = load_cache(request)
  auth_app = get_msal_app(cache)

  accounts = auth_app.get_accounts()
  if accounts:
    result = auth_app.acquire_token_silent(
      settings['scopes'],
      account=accounts[0])
    save_cache(request, cache)

    return result['access_token']

def remove_user_and_token ( request ):
  if 'token_cache' in request.session:
    del request.session['token_cache']

  if 'user' in request.session:
    del request.session['user']
  
