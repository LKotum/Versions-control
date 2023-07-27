from fastapi import FastAPI, HTTPException
from .modules.auth import *
from .modules.tokenControl import *

class app:
	def __init__(self, **kwargs):
		self.rs = kwargs['RESPONSE_SERVICE']
		self.config = kwargs['CONFIG']
		self.token_service = controller()
		self.auth_service = account(self.token_service)
		self.responses()

	def responses(self):
		@self.rs.get("/")
		def get_main():
			raise HTTPException(status_code=418)


		@self.rs.post("/auth")
		def post_auth(token_server, token_user):
			self.auth_service.authorize(token_server, token_user)

		@self.rs.post("/add/app/")
		def post_addApp(token_ACK):
			...

		@self.rs.post("/add/version/")
		def post_addVersion(token_ACK, token_app, version: str):
			...
