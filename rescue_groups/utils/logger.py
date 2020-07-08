import logging
import os

LOG_LEVEL = getattr(logging, os.environ.get("LOG_LEVEL", "NOTSET"))

logging.basicConfig(level=LOG_LEVEL)
log = logging.getLogger("rescue-groups")
log.addHandler(logging.StreamHandler())
log.setLevel(LOG_LEVEL)
