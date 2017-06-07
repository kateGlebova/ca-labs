import pickle
from os.path import dirname, join

from serialization.serializer_types import BinarySerializer


class PICKLESerializer(BinarySerializer):
    """
        A pickle calculator serializer.
    """
    _filename = 'data.p'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path)

    @staticmethod
    def s_load(f):
        """
        Wrap pickle loader function.
        :return: deserialized object
        """
        return pickle.load(f)

    @staticmethod
    def s_dump(obj, f):
        """
        Wrap pickle dumper function.
        :return: None
        """
        pickle.dump(obj, f)