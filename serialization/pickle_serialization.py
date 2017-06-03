import pickle
from os.path import dirname, join

from serialization.serialization import Serializer


class PICKLESerializer(Serializer):
    _filename = 'data.p'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path, 'rb')

    def s_load(self, f):
        return pickle.load(f)

    def s_dump(self, f):
        pickle.dump(self._obj, f)

    def dump(self):
        with open(self._path, 'wb') as f:
            self.s_dump(f)