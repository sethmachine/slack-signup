"""Manages the collection of Typeform results and subsequent Slack invitations.

.. moduleauthor:: Seth-David Donald Dworman <sdworman@brandeis.edu>

"""

import json
import requests

import fileutils
import slack
import typeform

INVITED_EMAILS = 'secret/invited-emails.txt'

def invite_to_scums(invited_emails=INVITED_EMAILS):
    already_invited = fileutils.read_list(invited_emails)
    signups = typeform.get_scums_signups()
    new_emails = []
    responses = []
    for s in signups:
        email, username = s['email'], s['username']
        if not email:
            continue
        if email in already_invited:
            continue
        new_emails.append(email)
        response = slack.invite_to_scums(email, username)
        responses.append(response)
    fileutils.write_list(invited_emails, already_invited + new_emails)
    return {'new_emails':new_emails, 'responses':responses}

if __name__ == '__main__':
    d = invite_to_scums()
