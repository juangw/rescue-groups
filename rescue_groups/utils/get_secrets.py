import pkg_resources
import json
import os

STAGE = os.environ.get("STAGE", "local")


def get_secret():
    return pkg_resources.resource_string(__name__, "../../secrets.json")


def get_api_key(topic: str):
    if STAGE == "local":
        secrets = get_secret().decode()
        topic_secret = json.loads(secrets).get(topic)
        topic_api_key = topic_secret.get("api_key", "")
    else:
        topic_api_key = os.environ.get("{}_api_key".format(topic), "")
    return topic_api_key
