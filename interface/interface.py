from view import View


class Interface:
    def __init__(self, srlzr):
        self._serializer = srlzr
        self._view = View()

    def launch(self):
        raise NotImplementedError()