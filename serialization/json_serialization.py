import json

from os.path import dirname, join

from serialization.serialization import Serializer


class JSONSerializer(Serializer):
    _filename = 'data.json'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path)

    def s_load(self, f):
        return json.load(f)

    def s_dump(self, f):
        json.dump(self._obj, f)
