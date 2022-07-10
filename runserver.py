import os

from src import app


if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "0.0.0.0")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5000  # Would be an issue for mac user -> System preference, Sharing, Disable Airplay Receiver
    app.secret_key = ""
    app.run(HOST, PORT, debug=True)
