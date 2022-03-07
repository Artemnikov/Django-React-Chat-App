import requests
import json

graph_url = 'https://graph.microsoft.com/v1.0/me'

def get_user(token):
    # Send GET to /me
    user = requests.get('{}'.format(graph_url),
    headers={'Authorization': 'Bearer {0}'.format(token)},
    params={'$select':'displayName,mail,mailboxSettings,userPrincipalName'})
    return user.json()