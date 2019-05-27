import pkg_resources


def get_secret():
    return pkg_resources.resource_string(__name__, "../../secrets.json")
