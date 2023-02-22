from core.src.common.helpers.singleton import Singleton


class Logger(metaclass=Singleton):
    def __init__(self, run_id: str):
        self.run_id = run_id

    def log_step(self, func):
        raise NotImplementedError
