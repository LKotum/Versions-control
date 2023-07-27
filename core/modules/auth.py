from dataclasses import dataclass, field
from .tokenControl import *

@dataclass
class role():
	""" """
	role_name: str = None

	def __post_init__(self):
		match self.role_name:
			case "User":
				...
			case "Admin":
				...
			case _:
				raise Exception("Invalid role type")


class account:
	def __init__(self, token_service):
		self.token_service = token_service

	def register(self, admin_token, newUserName, role_name):
		newRole = role(role_name)
	
	def authorize(self, server_token, user_token):
		server_token_status = self.token_service.checkToken(server_token)
		user_token_status = self.token_service.checkToken(user_token)
		if (server_token_status == 200 and user_token_status == 200):
			return self.token_service.getTempToken(user_token)
