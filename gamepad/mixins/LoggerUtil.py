import logging

class LoggerMixIn():
    """ LoggerMixIn is used to standardize logging throughout gamepad """

    def __init__(self):
        """ setup default logging """
        # string constants
        self._logger_name = 'gamepad.mixins.LoggerMixIn'
        self._logger_format = '%(levelname)8s -- %(asctime)s -- %(message)s'
        # default handler
        self._logger = logging.getLogger(self._logger_name)
        log_handler = logging.FileHandler(self._logger_name+".log")
        # log level & format
        self._logger.setLevel(logging.DEBUG)
        log_formatter = logging.Formatter(self._logger_format)
        log_handler.setFormatter(log_formatter)
        # clear & configure
        self._logger.handlers = []
        self._logger.addHandler(log_handler)

    def get_logger(self):
        """ get logger """
        return self._logger
