class Singleton(object):
    """
    A simple singleton implementation
    """
    __shared_state = dict()

    def __init__(self):
        self.__dir__ = self.__shared_state


class RegistryInstance(object):

    instance = None

    class __Singleton(object):

        REGISTRY = None
        def __init__(self):
            self.REGISTRY = dict()

        def set(self, key, value):
            self.REGISTRY[key] = value

        def get(self, key):
            return self.REGISTRY.get(key)

    def __new__(cls):
        if(None is RegistryInstance.instance):
            RegistryInstance.instance = RegistryInstance.__Singleton()

        return RegistryInstance.instance

    def set(self, key, value):
        self.instance.set(key, value)

    def get(self, key):
        return self.instance.get(key)


class SingletonMetaClass(type):
    instance = None

    def __init__(cls, name, bases, dict):
        super(SingletonMetaClass, cls).__init__(name, bases, dict)
        new_function = cls.__new__

        def getInstance(cls, *args, **kwds):
            if(None is cls.instance):
                cls.instance = new_function(cls, *args, **kwds)

            return cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(getInstance)


class Registry(type):

    INSTANCE = dict()

    def __new__(cls, name, bases, attrs):
        type_class = type.__new__(cls, name, bases, attrs)
        cls.INSTANCE[type_class.__name__] = type_class

        return type_class

    @classmethod
    def setValue(cls, key, value):
        pass

    @classmethod
    def getValue(cls, key):
        pass
