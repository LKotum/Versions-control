import random, string
import secrets
from fastapi import HTTPException
import logging
import time

class controller:
	def __init__(self):
		"""
		The function initializes an object and checks for the existence of a root token, generating one if
		it is missing.
		"""
		self._SECRET = None
		#Checking for the root token
		if(not self.checkToken("root")):
			#If the root token is not found, create it
			self._SECRET = self._genSecret_()
			value = self._genToken_(target_type="root", object_name="root", secret=self._SECRET)
			if (value != 200):
				...
			#"!!!The root token is missing!!!"
			#logging ...

	def _genSecret_(self) -> str:
		"""
		The function `_genSecret_` generates a random 16-character lowercase string to be used as a System
		token for security purposes.
		:return: a randomly generated string of 16 lowercase letters.
		"""
		secret = string.ascii_lowercase
		return ''.join(random.choice(secret) for i in range(16))

	def _genToken_(self, target_type, object_name, secret: str = None) -> str:
		# Generating a token for root
		if (target_type == "root" and self._SECRET is not None):
			# Checking the temporary system key
			if self._SECRET == secret:
				token = secrets.token_hex(256)
				# Terminate the function after creating root
				return "200"
		match target_type:
			case "user":
				token = secrets.token_urlsafe(32)
			case "app":
				token = secrets.token_urlsafe(32)
			case "server":
				token = secrets.token_urlsafe(32)
			case "temp":
				token = secrets.token_urlsafe(32)
				# Save to base

				return token
			case _:
				# "Invalid value target_type"
				raise HTTPException(status_code=400)

	def removeToken(self, token, user_token, ACKToken):
		...

	def checkToken(self, token) -> int: # 200 OK, 403 Forbidden (Incorrect or Unknown)
		...

	def setToken(self): # What does it do ???
		...

	def getToken(self, object_name, user_token):
		...

	def getTempToken(self, user):
		# Generate temp token
		temp_token = _genToken_(self, "temp", "user")
		# Return to user
		return temp_token


class synToken:
	def __init__(self):
		self._timers = {}

	def new(self):
		...

	def check(self):
		...

class cryptoController:
	def __init__(self):
		...