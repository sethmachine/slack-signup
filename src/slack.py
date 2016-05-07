"""Programmatically send an invite to a Slack team.

.. moduleauthor:: Seth-David Donald Dworman <sdworman@brandeis.edu>

"""

import json
import requests

import fileutils

SLACK_PROTOCOL = 'https://'
SLACK_URL = '.slack.com/api/'

INVITE_PATH = 'users.admin.invite'

SCUMS_CREDENTIALS = 'secret/scums.json'

def load_scums_credentials(json_file=SCUMS_CREDENTIALS):
    with open(json_file, 'r') as f:
        j = json.load(f)
    return j['token'], j['channels']

def invite(email, firstname, teamname, channels, token):
    url = SLACK_PROTOCOL + teamname + SLACK_URL + INVITE_PATH
    data = {'email':email, 'first_name':firstname,
            'channels':channels, 'token':token}
    response = requests.post(url, data=data)
    return response

def invite_to_scums(email, firstname, teamname='starcraftums'):
    token, channels = load_scums_credentials()
    return invite(email, firstname, teamname, channels, token)

if __name__ == '__main__':
    r = invite_to_scums('sethmachine01@gmail.com', 'sethmachine')
