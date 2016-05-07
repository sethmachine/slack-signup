"""Retrieves Typeform results.

.. moduleauthor:: Seth-David Donald Dworman <sdworman@brandeis.edu>

"""

import json
import requests

TYPEFORM_URL = 'https://api.typeform.com/v1/form/'


def load_credentials(json_file):
    with open(json_file, 'r') as f:
        j = json.load(f)
    return j['Starcraft UMS UID'], j['Typeform Key']

def get_results(uid, key):
    """Retrieves the Typeform results for a given survey's UID.

    """
    url = TYPEFORM_URL + uid + '?key=' + key
    response = requests.get(url)
    return json.loads(response.text)

def get_signups(uid, key):
    """Hardcoded read method for Starcraft UMS survey.

    """
    j = get_results(uid, key)['responses']
    signups = []
    for r in j:
        answers = r['answers']
        username = answers['textfield_21959449']
        email = answers['email_21959452']
        signups.append({'username':username, 'email':email})
    return signups

if __name__ == '__main__':
    uid, key = load_credentials('secret/credentials.json')
    s = get_signups(uid, key)
