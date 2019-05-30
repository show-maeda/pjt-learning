# Python3とRequestsで郵便番号から住所を取得するAPIを叩く
# https://www.taillook.tech/entry/python3-requests-zipcloud


import json
import sys
import requests

def main( zipcode ):
  url = "http://zipcloud.ibsnet.co.jp/api/search"
  param = { "zipcode": zipcode }

  res = requests.get( url, params = param )
  # json → dictionary
  response = json.loads( res.text )
  address = response["results"][0]

  print( address["address1"] + address["address2"] + address["address3"] )
  print( response )

# python3 main.py zipcode
# ex) python3 main.py 1900003
main( sys.argv[1] )