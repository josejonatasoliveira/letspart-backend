from rest_framework.exceptions import APIException

class UserNotFound(APIException):
  status_code = 404
  default_detail = "User not found!"
  default_code = "1120ade9-e9ee-4e77-a094-b603d70294a4"

class TokenNotFound(APIException):
  status_code = 404
  default_detail = "Token not found!"
  default_code = "29fcc743-ff53-47dd-89ac-cef4812f137b"