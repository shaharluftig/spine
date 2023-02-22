import logging
import sys
import time
from functools import wraps

from core.src.common.helpers.singleton import Singleton


class CardoLogger(metaclass=Singleton):
    def __init__(self, run_id: str, name: str = "CardoLogger"):
        self.run_id = run_id
        self.setup_logger()
        self.logger = logging.getLogger(name)

    def setup_logger(self):
        logging.basicConfig(level=logging.INFO, handlers=[
            logging.StreamHandler(sys.stdout)], format=f'{self.run_id} | %(asctime)s %(levelname)s | %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def log_step(self, func):
        @wraps(func)
        async def step_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = await func(*args, **kwargs)
            end_time = time.perf_counter()
            self.logger.info(f'Step {func.__qualname__.split(".")[0]} '
                             f'Took {end_time - start_time:.4f} seconds')
            return result

        return step_wrapper
