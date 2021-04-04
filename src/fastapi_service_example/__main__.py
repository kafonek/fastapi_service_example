import os

import uvicorn

if __name__ == "__main__":
    from .app import app

    uvicorn.run(
        app,
        host=os.getenv("SERVICE_HOST", "0.0.0.0"),
        port=int(os.getenv("SERVICE_PORT", 8181)),
    )
