# encoding: utf-8
import os
from decouple import config
from datetime import datetime


# MICROSOFT GRAPH API KEYS HERE!
APP_ID = config('APP_CLIENT_ID')
APP_SECRET  = config('APP_CLIENT_SECRET')
MS_GRAPH_API_URL  = 'https://graph.microsoft.com/v1.0/me'
AUTHORITY_URL = 'https://login.microsoftonline.com/consumers/'

# this block checks whether you have your keys written or not
if APP_ID == "" or APP_SECRET == "":
    print('\n\n##### \n\nPlease get an API key at the MICROSOFT GRAPH website! \n\n##### \n\n')
    raise ValueError



################################################################ SCOPES ->
SCOPES = [
    'Calendars.ReadWrite',
    'Calendars.ReadWrite.Shared',
    'Contacts.ReadWrite',
    'Contacts.ReadWrite.Shared',
    'Files.ReadWrite.All',
    'Files.ReadWrite.AppFolder',
    'Files.ReadWrite.Selected',
    'Mail.ReadWrite',
    'Mail.ReadWrite.Shared',
    'Mail.Send',
    'Mail.Send.Shared',
    'Notes.ReadWrite.All',
    'Notes.ReadWrite.CreatedByApp',
    'Tasks.ReadWrite',
    'Tasks.ReadWrite.Shared',
    'User.Export.All',
    'User.Invite.All',
    'User.ManageIdentities.All',
    'User.ReadWrite',
    'User.ReadWrite.All',
    'UserActivity.ReadWrite.CreatedByApp'
]



################################################################ PATHS ->
home = str(os.getcwd())

FILES_FOLDER = home + '/'
LOGS_PATH = FILES_FOLDER + 'logs/'
