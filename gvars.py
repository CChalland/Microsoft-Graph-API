# encoding: utf-8
import os
from decouple import config
from datetime import datetime


# MICROSOFT GRAPH API KEYS HERE!
APP_ID = config('APP_CLIENT_ID')
APP_SECRET = config('APP_CLIENT_SECRET')
AUTHORIZATION_CODE = config('AUTHORIZATION_CODE')


# AUTHORITY_URL = 'https://login.microsoftonline.com/consumers/'
# AUTHORITY_URL = 'https://login.microsoftonline.com/Enter_the_Tenant_Id_Here/adminconsent?client_id=Enter_the_Application_Id_Here'
AUTHORITY_URL = 'https://login.microsoftonline.com/207c78cf-645d-48ea-8a38-5f4754432b0d'
MS_GRAPH_API_URL  = 'https://graph.microsoft.com/v1.0/users'


# this block checks whether you have your keys written or not
if APP_ID == "" or APP_SECRET == "":
    print('\n\n##### \n\nPlease get an API key at the MICROSOFT GRAPH website! \n\n##### \n\n')
    raise ValueError



################################################################ SCOPES ->
SCOPES = [ "https://graph.microsoft.com/.default" ]
# SCOPES = [
#     'Calendars.ReadWrite',
#     'Calendars.ReadWrite.Shared',
#     'Contacts.ReadWrite',
#     'Contacts.ReadWrite.Shared',
#     'Files.ReadWrite.All',
#     'Files.ReadWrite.AppFolder',
#     'Files.ReadWrite.Selected',
#     'Mail.ReadWrite',
#     'Mail.ReadWrite.Shared',
#     'Mail.Send',
#     'Mail.Send.Shared',
#     'Notes.Create',
#     'Notes.ReadWrite.All',
#     'Notes.ReadWrite.CreatedByApp',
#     'Tasks.ReadWrite',
#     'Tasks.ReadWrite.Shared',
#     # 'User.Export.All',
#     # 'User.Invite.All',
#     # 'User.ManageIdentities.All',
#     'User.ReadWrite'
#     # 'User.ReadWrite.All'
# ]



################################################################ PATHS ->
home = str(os.getcwd())

FILES_FOLDER = home + '/'
LOGS_PATH = FILES_FOLDER + 'logs/'
