import json, requests

def sendSlack( url, param ):
  res = requests.post( url, data = json.dumps( param ) )
  # print( res, res.text )
  return res

# example param
#   param = {
#     'text': u'Hello World'
#     , 'username' : u'python'
#     , 'icon_emoji' : u':test_red:'
#     , 'link_names' : 1
#     , 'attachments' : [
#       {
#          'fallback' : 'fallback Test',
#          'pretext' : 'attachments Test',
#          'color' : '#D00000',
#          'fields' : [
#             {
#                'title' : 'attachment01',
#                'value' : 'This is attachment'
#             }
#          ]
#       }
#     ]
#   }