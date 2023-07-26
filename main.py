from core.app import app
from fastapi import FastAPI


response_service = FastAPI(
	title="Version controller"
)


Application = app(RESPONSE_SERVICE = response_service)
if __name__ == "__main__":
	Application.run()
