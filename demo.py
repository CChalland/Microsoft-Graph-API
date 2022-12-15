import gvars
import requests
import webbrowser
from msal import PublicClientApplication, ConfidentialClientApplication


# ## Method 1: Authenticatrion with authorization code
# client_instance = ConfidentialClientApplication(
#     client_id=gvars.APP_ID,
#     client_credential=gvars.APP_SECRET
# )
# # authorization_url = client_instance.get_authorization_request_url(gvars.SCOPES)
# # print(authorization_url)
# # webbrowser.open(authorization_url, new=True)
# # gvars.AUTHORIZATION_CODE = ''
# token = client_instance.acquire_token_by_authorization_code(
#     code=gvars.AUTHORIZATION_CODE,
#     scopes=gvars.SCOPES
# )

# headers = {'Authorization': 'Bearer ' + token['access_token']}
# response = requests.get(gvars.MS_GRAPH_API_URL + 'me', headers=headers)
# print(response.json())



## Method 2: Login to acquire access_token
app = PublicClientApplication(
    client_id=gvars.APP_ID,
    authority=gvars.AUTHORITY_URL
)

# accounts = app.get_accounts()
# if accounts:
#     app.acquire_token_silent(scopes=gvars.SCOPES, account=accounts[0])

flow = app.initiate_device_flow(scopes=gvars.SCOPES)
print(flow)
print(flow['message'])
webbrowser.open(flow['verification_uri'])

result = app.acquire_token_by_device_flow(flow)
headers = {'Authorization': 'Bearer ' + result['access_token']}
response = requests.get(gvars.MS_GRAPH_API_URL + 'me', headers=headers)
print(response.json())