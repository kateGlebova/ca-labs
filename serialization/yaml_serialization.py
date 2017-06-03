import yaml

from os.path import dirname, join

from serialization.serialization import Serializer


class YAMLSerializer(Serializer):
    _filename = 'data.yaml'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path)

    def s_load(self, f):
        return yaml.load(f)

    def s_dump(self, f):
        yaml.dump(self.obj, f)
