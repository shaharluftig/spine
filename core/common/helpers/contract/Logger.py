from core.common.helpers.contract.metaclasses.singleton import Singleton


class Logger(metaclass=Singleton):
    def __init__(self, run_id: str):
        self.run_id = run_id

    def time_function(self, func, msg: str):
        raise NotImplementedError
