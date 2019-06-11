import itchat
import requests
import json
url='http://openapi.tuling123.com/openapi/api/v2'
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    msg = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg['Text']
            }
        },
        "userInfo": {
            "apiKey": "cbfceae808b74609b249e4e90f7dc431",
            "userId": "www"
        }
    }
    dat = json.dumps(msg)
    res = requests.post(url, data=dat)
    res.encoding = 'utf-8'
    result = res.json()
    print(result)
    return result['results'][0]['values']['text']
itchat.auto_login()
itchat.run()
