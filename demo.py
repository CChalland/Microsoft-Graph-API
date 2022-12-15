import gvars
import requests
import webbrowser
from msal import PublicClientApplication, ConfidentialClientApplication


# Method 1: Authenticatrion with authorization code
client_instance = ConfidentialClientApplication(
    client_id=gvars.APP_ID,
    client_credential=gvars.APP_SECRET
)

# authorization_url = client_instance.get_authorization_request_url(gvars.SCOPES)
# print(authorization_url)
# webbrowser.open(authorization_url, new=True)
# gvars.AUTHORIZATION_CODE = ''


token = client_instance.acquire_token_by_authorization_code(
    code=gvars.AUTHORIZATION_CODE,
    scopes=gvars.SCOPES
)

headers = {'Authorization': 'Bearer ' + token['access_token']}

response = requests.get(gvars.MS_GRAPH_API_URL + 'me', headers=headers)
print(response.json())