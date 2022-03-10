import requests
import json
graph_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'

def get_user(user_id):
    # Send GET to /me
    user = requests.get('{}'.format(graph_url),
    data=json.dumps({'client_id': 'AAAAAAAAAAAAAAAAAAAAADAUMkKuuWalgiVqojzYgasdeA'}))
    
    return user