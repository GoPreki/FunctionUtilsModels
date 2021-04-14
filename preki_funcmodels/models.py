from neomodel import StructuredNode
from preki_funcutils import status
from preki_funcutils.exceptions import PrekiException


def assign_if_present(obj, dict, key):
    if key in dict and dict[key] is not None:
        setattr(obj, key, dict[key])
        return dict[key]


class PrekiNode(StructuredNode):
    __abstract_node__ = True

    @classmethod
    # @db.read_transaction
    def get_one(cls, id, raise_error=True):
        try:
            model = cls(id=id)
            model.refresh()
            if cls.__name__ not in model.labels():
                raise cls.DoesNotExist('Model Mismatch')
            return model
        except cls.DoesNotExist:
            if raise_error:
                raise PrekiException(f'{cls.__name__} not found (id={id})', status_code=status.HTTP_404_NOT_FOUND)
            else:
                return None

    @classmethod
    # @db.read_transaction
    def get_all(cls):
        return cls.nodes.all()

    @classmethod
    # @db.read_transaction
    def get_first(cls, data, raise_error=True):
        try:
            model = cls.nodes.first(**data)
            return model
        except cls.DoesNotExist:
            if raise_error:
                filter = {**data}
                raise PrekiException(f'{cls.__name__} not found ({filter})', status_code=status.HTTP_404_NOT_FOUND)
            else:
                return None
