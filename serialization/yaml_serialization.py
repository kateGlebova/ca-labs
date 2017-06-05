import yaml

from os.path import dirname, join

from serialization.serialization import Serializer


class YAMLSerializer(Serializer):
    """
        A yaml calculator serializer.

        Methods derived from Serializer class:

            add_bmr -- add BMR entry to the object.
            add_bmi -- add BMI entry to the object.
            add_calories -- add daily rate entry to the object.
            _dump -- _dump the object to the file.
    """
    _filename = 'data.yaml'

    def __init__(self, path=join(dirname(__file__), _filename)):
        super().__init__(path)

    def s_load(self, f):
        """
        Wrap yaml loader function.
        :return: deserialized object
        """
        return yaml.load(f)

    def s_dump(self, f):
        """
        Wrap yaml dumper function.
        :return: None
        """
        yaml.dump(self._obj, f)
