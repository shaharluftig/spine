import logging
import sys
import time
from functools import wraps

from core.common.helpers.logging.Logger import Logger


class GarnetLogger(Logger):
    def __init__(self, run_id: str, handlers=None, name: str = "GarnetLogger"):
        super().__init__(run_id)
        handlers = handlers if handlers else []
        self.handlers = handlers
        self.__setup_logger()
        self.logger = logging.getLogger(name)

    def __setup_logger(self):
        logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)] + self.handlers,
                            format=f'{self.run_id} | %(asctime)s %(levelname)s | %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def time_function(self, func, msg: str):
        @wraps(func)
        async def step_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = await func(*args, **kwargs)
            end_time = time.perf_counter()
            self.logger.info(f"{msg} Took {end_time - start_time:.4f} seconds")
            return result

        return step_wrapper
