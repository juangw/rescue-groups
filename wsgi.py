#!/usr/bin/env python3
from rescue_groups import create_app

import os

PORT = int(os.environ.get("PORT", 8080))

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
