def password_validator(password):
  import re
  regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
  aTOz0_9 = re.compile('[a-zA-Z0-9]')
  if password.isalpha():
        return 0
  if password.isnumeric():
        return 1
  if password.isalnum():
        return 2
  if regex.search(password) != None:
    if aTOz0_9.search(password) != None:
      return 3

password_validator("dehg@$%")

