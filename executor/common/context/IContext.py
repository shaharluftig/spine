class IContext:
    def get_context(self, *args, **kwargs):
        raise NotImplementedError
