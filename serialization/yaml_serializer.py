import yaml

from os.path import dirname, join

from serialization.serializer_types import TextSerializer


class YAMLSerializer(TextSerializer):
    """
        A yaml calculator serializer.e object.
    """
    _filename = 'data.yaml'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path)

    @staticmethod
    def s_load(f):
        """
        Wrap yaml loader function.
        :return: deserialized object
        """
        return yaml.load(f)

    @staticmethod
    def s_dump(obj, f):
        """
        Wrap yaml dumper function.
        :return: None
        """
        yaml.dump(obj, f)
