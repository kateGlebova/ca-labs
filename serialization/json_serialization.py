import json

from os.path import dirname, join

from serialization.serialization import Serializer


class JSONSerializer(Serializer):
    """
        A json calculator serializer.
    """
    _filename = 'data.json'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path)

    @staticmethod
    def s_load(f):
        """
         Wrap json loader function.
         :return: deserialized object
         """
        return json.load(f)

    @staticmethod
    def s_dump(obj, f):
        """
        Wrap json dumper function.
        :return: None
        """
        json.dump(obj, f)
