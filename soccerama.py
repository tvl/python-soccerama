#!/usr/bin/python
import requests
import json

api_token = ''
api_url = 'https://api.soccerama.pro/v1.2/'

def init(token):
    global api_token
    api_token = token

def get(endpoint, include=''):
    if include == '':
        payload = {'api_token': api_token }
    else:
        payload = {'api_token': api_token, 'include': include}
    r = requests.get(api_url + endpoint, params=payload)
    data = json.loads(r.text)
    return data

def matches(from_date, to_date = None, include = ''):
    """Get matches list"""
    if to_date is None:
        to_date = from_date
    return get('matches/{}/{}'.format(from_date, to_date), include)['data']

def countries():
    return get('countries')['data']

def competitions():
    return get('competitions')['data']

def seasons():
    return get('seasons')['data']


