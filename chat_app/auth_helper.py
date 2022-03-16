import yaml
import msal
import os
import time
import jwt

from base64 import b64decode
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


import requests
from rest_framework_jwt.utils import jwt_decode_handler
options = {
    'clockTolerance': 60*24*10,
    "audience": "300579e3-4a79-4fd2-8f09-60ed83326dd6",
    "issuer": "",
    "verify_signature": "RS256"
};
kid = ''
x5c = ''

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

# def get_msal_app(cache=None):
  # Initialize the MSAL confidential client
  # auth_app = msal.ConfidentialClientApplication(
  #   settings['app_id'],
  #   authority = 'https://login.microsoftonline.com/common',
  #   client_credential = settings['app_secret'],
  #   token_cache = cache)
  # return auth_app


def get_msal_app ( cache=None ):
  # Initialize the MSAL confidential client
  auth_app = msal.ConfidentialClientApplication (
    '300579e3-4a79-4fd2-8f09-60ed83326dd6',
    'kWe7Q~YiJxe0QOjZ-K.3hDUDfutYmzSucU1TA',
    authority = "https://login.microsoftonline.com/common",
    validate_authority=True,
    token_cache=False,
    http_client=None,
    verify=True,
    proxies=None,
    timeout=None,
    client_claims=None,
    app_name=None,
    app_version=None,
    client_capabilities=None,
    azure_region=None,
    exclude_scopes=None,
    http_cache=None
  )
  return auth_app

# Method to generate a sign-in flow
def get_sign_in_flow () :
  auth_app = get_msal_app()
  return auth_app.initiate_auth_code_flow(
    settings['scopes'],
    redirect_uri=settings['redirect'])

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
  
def validate ( token ):
  headers = jwt.get_unverified_header(token)
  kid = headers.get('kid')
  keys = requests.get('https://login.microsoftonline.com/common/discovery/v2.0/keys')
  keyList = keys.json().get('keys')
  for x in keyList:
    if x.get('kid') == kid:
      x5c = b64decode(x.get('x5c')[0])
      options['issuer'] = x.get('issuer')
  try:
    cert = x509.load_der_x509_certificate(x5c, default_backend())
    public_key = cert.public_key()  
    pem_key = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    verified = jwt.decode(token, pem_key, options)
  except Exception as e:
    print(e)
  return True
    