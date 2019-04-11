from common.utils.get_secrets import get_secret
from collections import namedtuple

import json

REQUEST = namedtuple("request_data", ["url", "data", "api_key"])


def get_api_key(topic):
    """Gets api key based on url"""
    secrets = get_secret().decode()
    topic_secret = json.loads(secrets).get(topic)
    topic_url = topic_secret.get("url")
    topic_data = topic_secret.get("data")
    topic_api_key = topic_secret.get("api_key", "")
    return REQUEST(topic_url, topic_data, topic_api_key)
