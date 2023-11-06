from flask import Flask
from src.Web.Routers.healthcheck import healthcheck_bp

class Startup:        

    def main(self) -> Flask:
        app = Flask(__name__)
        
        app.register_blueprint(healthcheck_bp)

        return app

