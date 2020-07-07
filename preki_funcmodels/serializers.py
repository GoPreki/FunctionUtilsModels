from abc import ABC, abstractmethod
from functools import wraps


def serialize(Serializer, is_array=True, simple=True):

    if not hasattr(Serializer, 'data') and callable(Serializer.data):
        raise Exception('Serializer must have a data(simple?: bool) method')

    def func_wrapper(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if is_array:
                return [Serializer(v).data(simple=simple) for v in response]
            else:
                return Serializer(response).data(simple=simple)

        return wrapper

    return func_wrapper


class PrekiSerializer(ABC):

    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def simple(self):
        pass

    def detail(self):
        raise NotImplementedError('To use simple=False in serializer.data() must implement detail method')

    def data(self, simple=True):
        return self.simple() if simple else self.detail()
