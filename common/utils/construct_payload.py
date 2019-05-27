from common.utils.get_secrets import get_secret
from collections import namedtuple

import json
import os

STAGE = os.environ.get("STAGE", "local")
REQUEST = namedtuple("request_data", ["url", "data", "api_key"])


def get_api_key(topic):
    """Gets api key based on url"""
    if STAGE == "local":
        secrets = get_secret().decode()
        topic_secret = json.loads(secrets).get(topic)
        topic_url = topic_secret.get("url")
        topic_data = topic_secret.get("data")
        topic_api_key = topic_secret.get("api_key", "")
    else:
        topic_url = os.environ.get("url")
        topic_api_key = os.environ.get("api_key", "")
        topic_data = {
            "apikey": topic_api_key,
            "objectType": "animals",
            "objectAction": "publicSearch",
            "search": {
                "resultSort": "animalID",
                "resultOrder": "asc",
                "calcFoundRows": "Yes",
                "filters": [],
                "fields": []
            }
        }
    return REQUEST(topic_url, topic_data, topic_api_key)
