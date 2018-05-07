import os
import sys

# Required to load modules from vendored subfolder
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./vendored"))

import json
import requests
from logger import configure_logger

LOGGER   = configure_logger(__name__)
TOKEN    = os.environ['TELEGRAM_TOKEN']
CHAT     = os.environ['TELEGRAM_CHAT']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)

def msgTelegramBot(event, context):
    try:
        res        = json.dumps(event, indent=2, sort_keys=True)
        response   = "*Received cloudwatch event*\n\n```\n{}\n```".format(res)
        data       = {"text": response.encode("utf8"), "chat_id": CHAT , "parse_mode": "Markdown"}
        
        LOGGER.debug('Sending to telegram: {}'.format(response))

        #Send data:
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        LOGGER.error(e)

    return {"statusCode": 200}