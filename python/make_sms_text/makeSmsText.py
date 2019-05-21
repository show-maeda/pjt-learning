import csv
import json
import sys
import requests

def shortenUrl( target_url ):
  url = "https://api.acrt.jp/ibss/api/us/AU487253/"
  param = {
      'id' : 'E8V7itGgUMPc3'
    , 'pass' : 'pXPHMNfW'
    , 'url' : target_url
  }
  res = requests.post( url, params = param )
  return res.text

def getDataFormated(
  name, data
):
  if name == 'telno':
    return '0' + data
  elif name == 'url':
    return shortenUrl( data )
  else:
    return data

def main( ):
  with open('csv_sample.csv', encoding = 'utf_8' ) as f:
    reader = csv.reader( f )
    header = next( reader )
    index = []

    for j in header:
      j = j.replace( '\ufeff', '' )
      index.append( j )
    else:
      print(index)

    dict_data = {}
    for row in reader:
      for j ,index_name in enumerate( index ):
        dict_data[index_name] = getDataFormated( index_name, row[j] )
      else :
        print( dict_data )
        dict_data = {} # initialize


if __name__ == '__main__':
  main()
