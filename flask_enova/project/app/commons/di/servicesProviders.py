from dependency_injector.providers import Provider
from dependency_injector.providers import Singleton
from flask import Flask


class ApplicationServiceProvider(Provider):
    _factory = None
    __slots__ = ('_factory')

    def __init__(self):
        self._factory = Singleton(Flask)
        super(ApplicationServiceProvider, self).__init__()

    def __call__(self, *args, **kwargs):
        if None is not self.last_overriding:
            return self.last_overriding._provider(args, kwargs)

        return self._factory(*args, **kwargs)
