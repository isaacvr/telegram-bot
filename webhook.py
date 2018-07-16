from pprint import pprint
import requests
import json

settings = json.load( open('settings.json', 'r') );

bot_token = settings.bot_token
test_url = "{}/{}".format(settings.https_server, bot_token)

def get_url(method):
  return "https://api.telegram.org/bot{}/{}".format(bot_token, method)

r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))

pprint(r.status_code)
pprint(r.json())