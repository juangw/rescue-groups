from collections import namedtuple
from string import Template

import requests
import logging
import json

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

REQUEST = namedtuple("request_data", ["url", "data", "api_key"])


def get_api_key(topic):
    """Gets api key based on url"""
    with open("../secrets.json") as secrets:
        topic_secret = json.load(secrets).get(topic)
        topic_url = topic_secret.get("url")
        topic_data = topic_secret.get("data")
        topic_api_key = topic_secret.get("api_key", "")
        return REQUEST(topic_url, topic_data, topic_api_key)


def call_api_url(topic):
    """Sends get request to the given api url"""
    api_info = get_api_key(topic)
    api_url = api_info.url
    api_data = api_info.data
    api_key = api_info.api_key
    headers = {"x-api-key": api_key}
    response = requests.post(
            url=api_url, headers=headers, json=api_data, timeout=5
    )
    print(response.text)


if __name__ == '__main__':
    call_api_url("rescue_group")
