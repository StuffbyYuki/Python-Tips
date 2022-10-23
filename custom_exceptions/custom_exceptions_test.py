from custom_exceptions import YourOwnException

try:
    raise YourOwnException('This is your own custom exception!')
except YourOwnException as e:
    print(e)

