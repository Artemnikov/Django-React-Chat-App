import requests
import json
graph_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

def get_user(request):
    reponse = requests.post('{}'.format(graph_url),
    data=json.dumps({'client_id': '{0}'.format(request)})
    )
    print(reponse)
    
    return reponse