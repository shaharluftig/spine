import logging
import sys
import time
from functools import wraps

from core.src.common.helpers.singleton import Singleton

logging.basicConfig(level=logging.INFO, handlers=[
    logging.StreamHandler(sys.stdout)], format='%(asctime)s %(levelname)-6s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class CardoLogger(metaclass=Singleton):
    def __init__(self, name: str = "CardoLogger"):
        self.logger = logging.getLogger(name)

    def log_step(self, func):
        @wraps(func)
        def step_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            self.logger.info(f'Step {func.__qualname__.split(".")[0]} '
                             f'Took {end_time - start_time:.4f} seconds')
            return result

        return step_wrapper

    def get_logger(self):
        return self.logger


cardo_logger = CardoLogger()
