import json

from os.path import dirname, join

from serialization.serialization import Serializer


class JSONSerializer(Serializer):
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

    def s_load(self, f):
        """
         Wrap json loader function.
         :return: deserialized object
         """
        return json.load(f)

    def s_dump(self, f):
        """
        Wrap json dumper function.
        :return: None
        """
        json.dump(self._obj, f)
