#!/usr/bin/env python3
from rescue_groups import create_app

import os

PORT = int(os.environ.get("PORT", 8080))
# This allows us to use a plain HTTP callback
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, ssl_context="adhoc")
