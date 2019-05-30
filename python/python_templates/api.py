# api

import json, requests

def get( url, param ):
  return res = requests.get( url, params = param )

def post( url, param ):
  return res = requests.post( url, data = param )

def postJson( url, param ):
  return res = requests.post( url, data = json.dumps( param ) )