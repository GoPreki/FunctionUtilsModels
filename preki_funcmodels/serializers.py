from functools import wraps


def serialize(Serializer, is_array=True, simple=True):

    if not hasattr(Serializer, 'data') and callable(Serializer.data):
        raise Exception('Serializer must have a data(simple: bool) method')

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
