from common.utils.get_secrets import get_secret
from collections import namedtuple

import requests
import logging
import json

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

REQUEST = namedtuple("request_data", ["url", "data", "api_key"])


def get_api_key(topic):
    """Gets api key based on url"""
    secrets = get_secret().decode()
    topic_secret = json.loads(secrets).get(topic)
    topic_url = topic_secret.get("url")
    topic_data = topic_secret.get("data")
    topic_api_key = topic_secret.get("api_key", "")
    return REQUEST(topic_url, topic_data, topic_api_key)


def api_post_req(topic, filters=[], fields=[]):
    """Sends get request to the given api url"""
    api_info = get_api_key(topic)
    if filters:
        api_info.data["search"]["filters"].extend(filters)
    if fields:
        api_info.data["search"]["fields"].extend(fields)

    api_url = api_info.url
    api_data = api_info.data
    api_key = api_info.api_key
    headers = {"x-api-key": api_key}

    try:
        res = requests.post(
            url=api_url,
            headers=headers,
            json=api_data,
            timeout=10,
        )
        if res.status_code == 200:
            return res.text
        else:
            logger.error(f"Request failed with response: {res.status_code}")
    except Exception as e:
        logger.error(e)
