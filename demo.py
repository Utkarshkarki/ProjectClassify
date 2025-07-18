from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys



logging.info('Welcome to custom log')

try:
    a=2/0

except Exception as e:
    # logging.error(e)
    # logging.error("Divide by zero error")
    # logging.error("Error message: {0}".format(e))
    # logging.error("Error message: {0} and error type: {1}".format(e, type(e)))
    raise USvisaException(e, sys) from e
    # raise Exception(e) from e
    # raise USvisaException(e, sys) from e