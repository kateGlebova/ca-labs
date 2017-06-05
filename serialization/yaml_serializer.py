import yaml

from os.path import dirname, join

from serialization.serializer_types import TextSerializer


class YAMLSerializer(TextSerializer):
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
