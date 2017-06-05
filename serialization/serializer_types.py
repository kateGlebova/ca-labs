from serialization.base_serializer import Serializer


class TextSerializer(Serializer):
    _mode = ''

    def __init__(self, path):
        super().__init__(path)


class BinarySerializer(Serializer):
    _mode = 'b'

    def __init__(self, path):
        super().__init__(path)