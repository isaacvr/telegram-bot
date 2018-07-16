import requests
from flask import Flask, request
import json

settings = json.load( open('settings.json', 'r') );

app = Flask(__name__)

bot_token = settings["bot_token"]

def get_url(method):
  return "https://api.telegram.org/bot{}/{}".format(bot_token, method)

def process_message(update):
  data = {}
  data["chat_id"] = update["message"]["from"]["id"];
  data["text"] = "I can hear you!"
  r = requests.post(get_url("sendMessage"), data=data)

@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
  if request.method == "POST":
    update = request.get_json()
    if "message" in update:
      process_message(update)

    return "ok!", 200