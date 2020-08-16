from rescue_groups.utils.construct_payload import get_api_key
from rescue_groups.utils.logger import log

from typing import Iterator, Dict, Any

import requests

SAVED_FIELDS = [
    "animalID",
    "animalName",
    "animalSex",
    "animalGeneralAge",
    "animalDescription",
    "locationPostalcode",
    "animalColor",
    "animalEyeColor",
    "animalThumbnailUrl",
]


def api_post_req(
    topic: str,
    start: int,
    filters: Iterator[str] = [],
    fields: Iterator[str] = [],
    display_all: bool = False,
) -> Dict[str, Any]:
    """Sends get request to the given api url"""
    api_info = get_api_key(topic)
    api_info.data["search"]["resultStart"] = start
    if not display_all:
        api_info.data["search"]["resultLimit"] = 20
    if filters:
        api_info.data["search"]["filters"].extend(filters)
    if fields:
        api_info.data["search"]["fields"].extend(fields)

    api_url = api_info.url
    api_data = api_info.data
    api_key = api_info.api_key
    headers = {"x-api-key": api_key}
    res = requests.post(url=api_url, headers=headers, json=api_data, timeout=10)
    if res.status_code == 200:
        return res.text
    else:
        log.error(f"Request failed with response: {res.status_code}")


def animal_by_id_req(topic: str, animal_id: int) -> Dict[str, Any]:
    """Sends get request to the given api url"""
    api_info = get_api_key(topic)
    id_filter = [
        {"fieldName": "animalID", "operation": "equals", "criteria": animal_id}
    ]
    api_info.data["search"]["filters"].extend(id_filter)
    api_info.data["search"]["fields"].extend(SAVED_FIELDS)

    api_url = api_info.url
    api_data = api_info.data
    api_key = api_info.api_key
    headers = {"x-api-key": api_key}

    res = requests.post(url=api_url, headers=headers, json=api_data, timeout=10)
    if res.status_code == 200:
        return res.text
    else:
        log.error(f"Request failed with response: {res.status_code}")
