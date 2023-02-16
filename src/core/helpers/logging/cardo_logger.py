import logging
import sys

from src.core.helpers.singleton import Singleton

logging.basicConfig(level=logging.INFO, handlers=[
    logging.StreamHandler(sys.stdout)], format='%(asctime)s %(levelname)-6s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class CardoLogger(metaclass=Singleton):
    def __init__(self, name: str = "CardoLogger"):
        self.logger = logging.getLogger(name)

    def get_logger(self):
        return self.logger
