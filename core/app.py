from fastapi import FastAPI

class app:
	def __init__(self, **kwargs):
		self.rs = kwargs['RESPONSE_SERVICE']
		self.responses()

	def responses(self):
		@self.rs.get("/{server_token}/{app_token}")
		def get_app_latest_version(server_token, app_token):
			''' '''
			...


		@self.rs.post("/add_app/{server_token}")
		def add_app(server_token, user_token):
			''' '''
			...


		@self.rs.post("/rm-app/{server_token}/{app_token}")
		def rm_app(server_token, app_token, user_token):
			''' '''
			...


		@self.rs.post("/add_version/{server_token}/{app_token}")
		def add_app_version(server_token, app_token, user_token):
			''' '''
			...

