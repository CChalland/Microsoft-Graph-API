import gvars
import json
import logging
import requests
import webbrowser
from msal import PublicClientApplication, ConfidentialClientApplication


## Method 1: Authenticatrion with authorization code
app = ConfidentialClientApplication(
    client_id=gvars.APP_ID,
    authority=gvars.AUTHORITY_URL,
    client_credential=gvars.APP_SECRET
)

# The pattern to acquire a token looks like this.
result = None

# Firstly, looks up a token from cache
# Since we are looking for token for the current app, NOT for an end user,
# notice we give account parameter as None.
result = app.acquire_token_silent(gvars.SCOPES, account=None)

if not result:
    logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
    result = app.acquire_token_for_client(scopes=gvars.SCOPES)

if "access_token" in result:
    # Calling graph using the access token
    graph_data = requests.get(  # Use token to call downstream service
        gvars.MS_GRAPH_API_URL,
        headers={'Authorization': 'Bearer ' + result['access_token']}, ).json()
    print("Graph API call result: ")
    print(json.dumps(graph_data, indent=2))
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))  # You may need this when reporting a bug













# AUTHORIZATION_CODE = 'M.R3_BAY.0d984727-71f4-6800-eb7d-dcfc48c7ad28'
# token = app.acquire_token_by_authorization_code(
#     code=AUTHORIZATION_CODE,
#     scopes=gvars.SCOPES
# )

# headers = {'Authorization': 'Bearer ' + token['access_token']}
# response = requests.get(gvars.MS_GRAPH_API_URL + 'me', headers=headers)
# print(response.json())
# response = requests.get("https://graph.microsoft.com/v1.0/users/ctchalland@gmail.com/onenote/pages/0-8190dfe2ac24c34aa0572d0b0e337b19!1-9E5BF352FFB0D317!1854/content?includeIDs=true", headers=headers)
# print(response.url)
# print(response.content)

# with open('test.html', 'wb+') as f:
#     f.write(response.content)



## Method 2: Login to acquire access_token
# app = PublicClientApplication(
#     client_id=gvars.APP_ID,
#     authority=gvars.AUTHORITY_URL
# )

# # accounts = app.get_accounts()
# # if accounts:
# #     app.acquire_token_silent(scopes=gvars.SCOPES, account=accounts[0])

# flow = app.initiate_device_flow(scopes=gvars.SCOPES)
# print(flow)
# print(flow['message'])
# webbrowser.open(flow['verification_uri'])

# result = app.acquire_token_by_device_flow(flow)
# headers = {'Authorization': 'Bearer ' + result['access_token']}
# response = requests.get(gvars.MS_GRAPH_API_URL + 'me', headers=headers)
# print(response.json())