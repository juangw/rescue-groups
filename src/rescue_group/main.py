from common.utils.get_api_data import api_post_req

import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

logger.debug("Start of Program, Testing Debugger")


def main():
    text = api_post_req("rescue_group")
    print(text)


if __name__ == '__main__':
    main()
