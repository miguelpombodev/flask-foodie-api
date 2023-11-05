from flask import Flask

class Startup:

    def main(self) -> Flask:
        app = Flask(__name__)

        return app

