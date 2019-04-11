from common.utils.construct_payload import get_api_key
from api_projects.log import log

import requests


def api_post_req(topic, start, stop, filters=[], fields=[]):
    """Sends get request to the given api url"""
    api_info = get_api_key(topic)
    api_info.data["search"]["resultStart"] = start
    api_info.data["search"]["resultLimit"] = stop
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
            log.error(f"Request failed with response: {res.status_code}")
    except Exception as e:
        log.error(f"API call failed with text: {e}")
