from core.app import app
from fastapi import FastAPI
from core.modules.configControl import config

cfg = config(PATH_TO_AUTH_CONFIG = "./config/auth.ini", PATH_TO_SERVER_CONFIG = "./config/server.ini", PATH_TO_TOKENS_CONFIG = "./config/token.ini" )


response_service = FastAPI(
	title="Version controller"
)


Application = app(RESPONSE_SERVICE = response_service, CONFIG = cfg)
if __name__ == "__main__":
	Application.run()
