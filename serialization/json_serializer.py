import json
from os.path import dirname, join

from serialization.serializer_types import TextSerializer


class JSONSerializer(TextSerializer):
    """
        A json calculator serializer.

        Methods derived from Serializer class:

            add_bmr -- add BMR entry to the object.
            add_bmi -- add BMI entry to the object.
            add_calories -- add daily rate entry to the object.
            dump -- dump the object to the file.
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
