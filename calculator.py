from configparser import ConfigParser
from os.path import join, dirname

from interface.command_line import CommandLine
from interface.menu import Menu
from serialization.json_serializer import JSONSerializer
from serialization.pickle_serializer import PICKLESerializer
from serialization.yaml_serializer import YAMLSerializer


class Main:
    _formats = {'json': JSONSerializer, 'yaml': YAMLSerializer, 'pickle': PICKLESerializer}
    _interfaces = {'menu': Menu, 'command-line': CommandLine}

    def __init__(self, config_path):
        self._config_path = config_path
        self._config = self._get_config()
        self._serializer = self._load_serializer()
        self._interface = self._choose_interface()

    def _get_config(self):
        """
        Get the config object from the config file.
        """
        config = ConfigParser()
        config.read(self._config_path)
        return config

    def _load_serializer(self):
        """
        Instantiate a serializer class. Format is specified in the config object.
        :return: object of the BinarySerializer/TextSerializer subclass
        """
        s_format = self._config['serialization']['serialization_format']
        try:
            return self._formats[s_format]()
        except KeyError:
            raise Exception('%s serialization format is not supported.' % s_format)

    def _choose_interface(self):
        interface = self._config['interface']['interface_type']
        try:
            return self._interfaces[interface](self._serializer)
        except KeyError:
            raise Exception('%s interface is not supported.' % interface)

    def launch(self):
        self._interface.launch()


if __name__ == "__main__":
    Main(join(dirname(__file__), 'conf.ini')).launch()